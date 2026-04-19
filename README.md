# 🚀 Ask My Docs — Production-Grade RAG System

A **multi-session, production-ready Retrieval-Augmented Generation (RAG)** application that allows users to upload documents (PDF/DOCX) and interact with them through a conversational interface.

---

# 🧠 Features

* Hybrid Retrieval (**BM25 + Vector Search**)
* Cross-Encoder Reranking
* Multi-session chat (ChatGPT-like)
* Session-based document isolation
* Groq-powered fast LLM responses
* Streamlit UI + FastAPI backend

---

# 📁 Project Structure

```
rag-app/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── ingestion/
│   └── main.py
│
├── ui/
│   └── app.py
│
├── data/
│   ├── raw_docs/
│   ├── chroma/
│   └── processed/
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```
git clone https://github.com/your-username/rag-app.git
cd rag-app
```

---

## 2️⃣ Create Virtual Environment

### Windows

```
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Install Additional Required Packages (Important)

```
pip install langchain langchain-community langchain-core langchain-text-splitters
pip install langchain-huggingface langchain-chroma
pip install sentence-transformers chromadb fastapi uvicorn streamlit
pip install langchain-groq python-docx pypdf
```

---

## 5️⃣ Set Groq API Key

### Windows

```
setx GROQ_API_KEY "your_api_key_here"
```

### Mac/Linux

```
export GROQ_API_KEY="your_api_key_here"
```

Restart terminal after setting.

---

# 🧹 One-Time Cleanup (VERY IMPORTANT)

Before first run:

### Windows (PowerShell)

```
Remove-Item -Recurse -Force .\data\chroma
Remove-Item -Recurse -Force .\data\processed
```

### Mac/Linux

```
rm -rf data/chroma
rm -rf data/processed
```

---

# 🚀 Running the Project (STEP-BY-STEP)

## 🔴 STEP 1: Start Backend (MUST FIRST)

Open Terminal 1:

```
uvicorn app.main:app --reload
```

You should see:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## 🔍 Verify Backend

Open in browser:

```
http://localhost:8000/docs
```

If this opens → backend is working ✅

---

## 🟢 STEP 2: Start Streamlit UI

Open Terminal 2:

```
streamlit run ui/app.py
```

---

# 🧪 How to Use

1. Open Streamlit UI
2. Create a new chat session
3. Upload PDF/DOCX files
4. Click **"Process Documents"**
5. Ask questions

---

# ⚠️ Important Rules

## ✅ Always Run Backend First

```
Backend → THEN UI
```

If not:

```
ConnectionRefusedError ❌
```

---

# 🧠 Session Isolation

Each chat session has:

* Separate vector database
* Separate BM25 index
* Separate chat memory

👉 No data mixing across chats

---

# ❗ Common Errors & Fixes

## 1. Connection Refused

```
Error: localhost:8000 refused connection
```

### Fix:

```
Run backend first:
uvicorn app.main:app --reload
```

---

## 2. Wrong Answers / Mixed Data

### Fix:

```
Delete old data:
Remove-Item -Recurse -Force .\data\chroma
Remove-Item -Recurse -Force .\data\processed
```

---

## 3. Module Not Found

### Fix:

```
pip install -r requirements.txt
```

---

## 4. Groq API Error

### Fix:

```
Check API key:
echo %GROQ_API_KEY%
```

---

# 🔥 Example Workflow

```
1. Start backend
2. Start UI
3. Upload resume.pdf
4. Click Process
5. Ask: "What is the company name?"
6. Get accurate answer
```

---

# 🛠️ Tech Stack

* FastAPI (Backend)
* Streamlit (UI)
* ChromaDB (Vector DB)
* HuggingFace (Embeddings)
* BM25 (Keyword search)
* BGE Reranker
* Groq (LLM)

---

# 🚀 Future Improvements

* Query rewriting (better accuracy)
* Streaming responses (typing effect)
* Document viewer with highlights
* Cloud deployment (Docker, AWS)

---

# 👨‍💻 Author

Aditya Shirodkar
Computer Science Engineer | AI Developer

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

# 💥 Final Note

This is a **production-level RAG system** with:

* Hybrid retrieval
* Multi-session architecture
* Document isolation

👉 Similar to real-world enterprise AI systems.

---
