# 🎓 StudyAI

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-black)
![AI](https://img.shields.io/badge/AI-Gemini-orange)
![Hackathon](https://img.shields.io/badge/Microsoft-Agents%20League%202026-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 🎓 StudyAI

> AI-powered study workspace for chatting with PDFs using Gemini AI and Flask.

StudyAI is a clean, distraction-free AI study assistant that allows students to upload PDF study materials and interact with them through intelligent conversations.

Users can query individual documents or search across multiple files simultaneously using natural language.

Built for the **Agents League Hackathon 2026** hosted by Microsoft.

---

# 🚀 Features

## 📚 Multi-File AI Chat

* Upload multiple PDF files
* Chat with a single file or all files together
* Cross-reference information across documents

## 💡 Smart Suggestions

* Dynamic AI-generated study prompt chips
* Faster and easier interaction

## 🧹 Focus Mode

* Hide unnecessary panels
* Distraction-free workspace

## 📝 Session Export

* Download study conversations as `.txt` notes

## 🎨 Responsive UI

* Dark & Light themes
* Smooth animations
* Mobile-friendly interface

---

# 🛠️ Tech Stack

| Category       | Technology                      |
| -------------- | ------------------------------- |
| Backend        | Python, Flask                   |
| AI Model       | Gemini 3.5 Flash                |
| AI SDK         | Google GenAI SDK                |
| PDF Processing | PyPDF2                          |
| Frontend       | HTML5, CSS3, Vanilla JavaScript |

---

# ⚡ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sathidevivaraprasadreddy/StudyAI.git
cd StudyAI
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 4️⃣ Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# 📂 Project Structure

```text
StudyAI/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── .env
│
├── uploads/
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── img1.png
├── img2.png
│
└── __pycache__/
```

---

# 📸 Screenshots

## Dashboard

![Dashboard](img1.png)

## Chat Interface

![Chat Interface](img2.png)

---

# 🏆 Hackathon Submission

### Event

Agents League Hackathon 2026

### Hosted By

Microsoft

### Track

Reasoning Agents

### Focus

AI-powered educational reasoning and document interaction.

---

# 🔒 Security

Never upload your `.env` file publicly.

Add this to `.gitignore`:

```gitignore
.env
__pycache__/
uploads/
```

---

# 🌟 Future Improvements

* OCR support for scanned PDFs
* AI-generated quizzes
* Flashcard generation
* Voice interaction
* Cloud sync support

---

# 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork repository
2. Create feature branch
3. Commit changes
4. Open pull request

---

# 📄 License

MIT License

---

# ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub.

