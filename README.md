# 🤖 LISA — Virtual Assistant

LISA is a **terminal-based AI virtual assistant** powered by the **Google Gemini API**. It provides a simple command-line interface for interacting with Gemini models while maintaining conversation context across multiple turns.

The project was built to explore **LLM API integration, conversational context management, model selection, environment-based API key security, and CLI application development**.

## ✨ Features

* 💬 **Multi-turn conversations** — LISA maintains conversation history so responses can use previous messages as context.
* 🤖 **Gemini-powered responses** — Uses Google's Gemini API to generate AI responses.
* 🔄 **Model selection** — Choose the Gemini model to use when starting the application.
* 💻 **Terminal-based interface** — Lightweight and easy to run directly from the command line.
* 🛑 **Simple exit commands** — End the conversation using `exit`, `quit`, or `stop`.
* 🔐 **Secure API key management** — API credentials are stored in a `.env` file and excluded from Git using `.gitignore`.
* ⚡ **Minimal setup** — Designed to be easy to install and run locally.

## 🛠️ Tech Stack

* **Python**
* **Google Gemini API**
* **Google GenAI Python SDK**
* **python-dotenv**
* **Git & GitHub**

## 📁 Project Structure

```text
lisa-virtual-assistant/
│
├── main.py              # Main application
├── requirements.txt     # Python dependencies
├── .gitignore           # Prevents sensitive files from being committed
└── .env                 # API key (local only, not included in GitHub)
```

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Shubhamshahni/lisa-virtual-assistant.git
cd lisa-virtual-assistant
```

### 2. Create a virtual environment

It is recommended to use a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Create a file named `.env` in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

LISA loads the API key from the environment rather than storing the secret directly in the source code.

> **Security:** Never commit your `.env` file or expose your API key publicly.

### 5. Run LISA

```bash
python main.py
```

## 💻 Example

```text
1: Gemini Model 1
2: Gemini Model 2
3: Gemini Model 3
4: Gemini Model 4

Select Gemini Model: 1

*************************************************************
Model in Use: Gemini Model 1
to End Chat: exit, stop or quit

Gemini: Hello! How can I help you today?

You: What is machine learning?

Gemini: Machine learning is a branch of artificial intelligence...
```

The conversation continues until the user enters:

```text
exit
```

or:

```text
quit
```

or:

```text
stop
```

## 🧠 How It Works

LISA follows a simple conversational pipeline:

```text
User Input
    │
    ▼
Terminal Interface
    │
    ▼
Conversation History
    │
    ▼
Google Gemini API
    │
    ▼
Generated Response
    │
    ▼
Terminal Output
    │
    └──────────► Conversation History
```

Each user message and generated response is added to the conversation context. This allows LISA to maintain context across multiple turns rather than treating every message as an isolated request.

## 🔐 Security

The Gemini API key is **not stored directly in ****`main.py`**.

Instead, it is stored locally in:

```text
.env
```

The `.gitignore` file prevents `.env` from being uploaded to GitHub.

Example:

```text
.env
```

> Never share your API key in source code, screenshots, Git commits, or public repositories.

## 🚀 Future Improvements

Planned improvements include:

* [ ] Add robust API and network error handling
* [ ] Validate model selection and user input
* [ ] Add conversation clearing commands
* [ ] Add conversation persistence
* [ ] Improve terminal UI and formatting
* [ ] Add configurable system instructions/personality
* [ ] Add logging
* [ ] Add automated tests
* [ ] Improve context/token management
* [ ] Add support for additional Gemini capabilities

## 🎯 Learning Goals

This project was created to gain practical experience with:

* Integrating a third-party AI API
* Working with large language models
* Managing conversational context
* Building command-line applications
* Managing environment variables and secrets
* Handling Python dependencies
* Using Git and GitHub for version control

## 👨‍💻 Author

**YOUR NAME**

GitHub: `https://github.com/Shubhamshahni`

---

⭐ If you find this project interesting, consider giving the repository a star.
