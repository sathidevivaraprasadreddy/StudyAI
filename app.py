import os
from flask import Flask, render_template, request, jsonify
from PyPDF2 import PdfReader
from google import genai
from dotenv import load_dotenv

load_dotenv()
ai_client = genai.Client()

app = Flask(__name__)
UPLOAD_DIR = 'uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

my_storage = {}
active_file = "all_files_together"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    global active_file
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded.'}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected.'}), 400

    if file and file.filename.endswith('.pdf'):
        name = file.filename
        save_path = os.path.join(UPLOAD_DIR, name)
        file.save(save_path)
        
        try:
            reader = PdfReader(save_path)
            extracted_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"
            
            my_storage[name] = extracted_text
            active_file = name
            
            suggestions = [
                "Summarize the key points of this document.",
                "What are the most important dates or deadlines mentioned?",
                "Give me a 3-bullet briefing on this file."
            ]
            
            return jsonify({
                'message': f'"{name}" uploaded successfully!',
                'active_file': name,
                'available_files': list(my_storage.keys()),
                'raw_text': extracted_text,
                'suggestions': suggestions
            })
            
        except Exception as e:
            return jsonify({'error': f'Could not read PDF: {str(e)}'}), 500
            
    return jsonify({'error': 'Please upload a PDF file.'}), 400

@app.route('/switch_file', methods=['POST'])
def switch_file():
    global active_file
    data = request.get_json() or {}
    target = data.get('filename')
    
    if target == "all_files_together":
        active_file = target
        return jsonify({
            'message': 'Now searching across all uploaded files at the same time.',
            'active_file': target,
            'available_files': list(my_storage.keys()),
            'raw_text': "--- ALL FILES SELECTED ---\nShowing combined data from everything you uploaded.",
            'suggestions': ["Summarize all documents combined.", "What tasks are due next across all files?"]
        })
        
    if target in my_storage:
        active_file = target
        return jsonify({
            'message': f'Now searching only inside: {target}',
            'active_file': target,
            'available_files': list(my_storage.keys()),
            'raw_text': my_storage[target],
            'suggestions': ["Summarize this document.", "List the deadlines here.", "Explain the main requirements."]
        })
        
    return jsonify({'error': 'File not found.'}), 404

@app.route('/reset', methods=['POST'])
def reset_workspace():
    global my_storage, active_file
    my_storage.clear()
    active_file = "all_files_together"
    return jsonify({'message': 'Workspace reset successful.'})

@app.route('/ask', methods=['POST'])
def ask_question():
    global active_file
    data = request.get_json() or {}
    question = data.get('question')
    
    if not question:
        return jsonify({'error': 'Please type a question.'}), 400

    if active_file == "all_files_together":
        if not my_storage:
            return jsonify({'error': 'Please upload at least one PDF first.'}), 400
        combined_text = ""
        for name, text in my_storage.items():
            combined_text += f"\n\n--- From File: {name} ---\n{text}"
        context = combined_text
        source_label = "All Files Together"
    else:
        context = my_storage.get(active_file, "")
        source_label = active_file

    if not context:
        return jsonify({'error': 'No text found to read.'}), 400

    try:
        rules = (
            "You are a helpful assistant.\n"
            "Answer the question step-by-step using ONLY the provided text below.\n"
            "If the answer is not in the text, say 'Answer not found in the documents'.\n"
            f"At the very end, write exactly: [Source: {source_label}]"
            f"\n\nText:\n{context}"
        )
        
        response = ai_client.models.generate_content(
            model='gemini-3.5-flash',
            contents=question,
            config={'system_instruction': rules}
        )
        return jsonify({'answer': response.text})
        
    except Exception as primary_error:
        print(f"Primary engine timeout: {str(primary_error)}")

    try:
        rules = f"Read this text:\n{context}\n\nQuestion: {question}\nAnswer:"
        try:
            res = ai_client.models.generate_content(model='gemini-2.5-flash', contents=rules)
            return jsonify({'answer': f"*(Using Backup Model 2.5)*\n\n{res.text}\n\n[Source: {source_label}]"})
        except Exception:
            res = ai_client.models.generate_content(model='gemini-1.5-flash', contents=rules)
            return jsonify({'answer': f"*(Using Backup Model 1.5)*\n\n{res.text}\n\n[Source: {source_label}]"})
            
    except Exception as final_error:
        return jsonify({'error': f'The AI servers are temporarily down: {str(final_error)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)