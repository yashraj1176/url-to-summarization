# 🎥 URL & YouTube Summarizer

An AI-powered web application that summarizes content from websites and YouTube videos using **LangChain, Groq LLM, and Streamlit**.

## 🚀 Features

* 🌐 Summarize website URLs
* ▶️ Summarize YouTube videos
* 🤖 Powered by Groq LLM
* 🔗 Built using LangChain
* ⚡ Fast AI-powered summarization
* 🖥️ Simple Streamlit interface
* 🔐 Groq API key entered securely through the application

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* LangChain Community
* LangChain Groq
* Groq API
* YouTube Transcript API
* Unstructured
* Validators

## 📂 Project Structure

```text
url-to-summarization/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd url-to-summarization
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run main.py
```

## 🔑 Groq API Key

You need a Groq API key to use the application.

When the application starts, enter your API key in the sidebar.

**Never upload your API key or other secrets to GitHub.**

## 🧠 How It Works

```text
User enters URL
       ↓
URL validation
       ↓
Website / YouTube detection
       ↓
Content extraction
       ↓
LangChain summarization chain
       ↓
Groq LLM
       ↓
Generated summary
       ↓
Displayed in Streamlit
```

## 🤖 Model

This project uses the Groq-hosted:

```text
openai/gpt-oss-20b
```

## 📸 Application

Add screenshots of your Streamlit application here.

```text
screenshots/
└── app.png
```

## 🎯 Future Improvements

* Add multiple summarization modes
* Add summary length selection
* Add downloadable summaries
* Add PDF export
* Add chat-based interaction with the extracted content
* Deploy the application online

## 👨‍💻 Author

**Yashraj Rathore**

B.Tech CSE Student | AI/ML Enthusiast
