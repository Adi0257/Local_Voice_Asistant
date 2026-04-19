# 🚀 Ask My Docs — Production RAG System

A **multi-session Retrieval-Augmented Generation (RAG)** application that allows users to upload documents (PDF/DOCX) and chat with them intelligently.

This system implements **hybrid retrieval (BM25 + vector search), reranking, and session-based isolation**, similar to real-world enterprise AI systems.

---

# 🧠 Features

* 🔍 Hybrid Retrieval (**BM25 + ChromaDB vector search**)
* ⚡ Cross-Encoder Reranking (BGE Reranker)
* 💬 Multi-session chat (ChatGPT-like UI)
* 📄 PDF & DOCX document ingestion
* 🔒 Session-based document isolation (no data mixing)
* ⚡ Fast LLM responses using **Groq (LLaMA3)**

---

# 🏗️ Architecture

```text
User (Streamlit UI)
        ↓
FastAPI Backend
        ↓
Hybrid Retrieval (BM25 + Vector DB)
        ↓
Reranker (Cross Encoder)
        ↓
Groq LLM (LLaMA3)
        ↓
Answer + Sources
```

---

# 📁 Project Structure

```text
RAG-APP/
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

```bash
git clone https://github.com/Adi0257/Local_Voice_Asistant.git
cd Local_Voice_Asistant
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install Extra Required Packages

```bash
pip install langchain langchain-community langchain-core langchain-text-splitters
pip install langchain-huggingface langchain-chroma
pip install sentence-transformers chromadb fastapi uvicorn streamlit
pip install langchain-groq python-docx pypdf
```

---

# 🔐 API Key Setup

⚠️ The Groq API key is currently **hardcoded inside the project**:

```text
app/core/generator.py
```

> Note: For production use, it is recommended to store API keys using environment variables.

---

# 🧹 One-Time Cleanup (Important)

Before running for the first time:

### Windows

```bash
Remove-Item -Recurse -Force .\data\chroma
Remove-Item -Recurse -Force .\data\processed
```

---

# 🚀 Running the Project

## 🔴 Step 1: Start Backend

```bash
cd app
cd ..
uvicorn app.main:app --reload
```

👉 Backend runs at:

```text
http://localhost:8000
```

---

## 🟢 Step 2: Start UI (New Terminal)

```bash
cd ui
streamlit run app.py
```

---

# ⚠️ IMPORTANT

Always follow this order:

```text
1. Start Backend
2. Start UI
```

If not:

```text
ConnectionRefusedError ❌
```

---

# 🧪 How to Use

1. Open Streamlit UI
2. Create a new chat session
3. Upload PDF/DOCX files
4. Click **"Process Documents"**
5. Ask questions

---

# 🧠 Example Queries

```text
- What is the name of the person?
- Which company does he work for?
- What skills are mentioned?
```

---

# 🔒 Session Isolation

Each chat session:

* Uses a separate Chroma collection
* Has its own BM25 index
* Maintains independent chat history

👉 No mixing between documents

---

# ❗ Common Errors

## ❌ Backend Not Running

```text
ConnectionRefusedError
```

### Fix:

```bash
uvicorn app.main:app --reload
```

---

## ❌ Wrong Answers

### Fix:

```bash
Remove-Item -Recurse -Force .\data\chroma
Remove-Item -Recurse -Force .\data\processed
```

---

# 🛠️ Tech Stack

* FastAPI (Backend)
* Streamlit (Frontend)
* ChromaDB (Vector DB)
* HuggingFace Embeddings (BGE)
* BM25 Retriever
* Cross Encoder Reranker
* Groq LLM (LLaMA3)

---

# 🚀 Future Improvements

* Query rewriting (better accuracy)
* Streaming responses (typing effect)
* Document viewer with highlights
* Deployment (Docker + Cloud)

---

# 👨‍💻 Author

Aditya Shirodkar
Computer Science Engineer | AI Developer

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

# 💥 Final Note

This is a **production-style RAG system** implementing:

* Hybrid retrieval
* Multi-session architecture
* Document-level isolation

👉 Similar to systems used in real-world AI applications.
