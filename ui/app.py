import streamlit as st
import requests
import os
import uuid

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Ask My Docs", layout="wide")

# ---------------- INIT ----------------
if "sessions" not in st.session_state:
    st.session_state.sessions = {}

if "current_session" not in st.session_state:
    session_id = str(uuid.uuid4())
    st.session_state.current_session = session_id
    st.session_state.sessions[session_id] = {
        "name": "Chat 1",
        "chat_history": [],
        "sources": []
    }

# ---------------- SIDEBAR ----------------
st.sidebar.title("💬 Chats")

# 🔁 Switch chats
for sid, data in st.session_state.sessions.items():
    if st.sidebar.button(data["name"], key=sid):
        st.session_state.current_session = sid

# ➕ New Chat
if st.sidebar.button("🆕 New Chat"):
    new_id = str(uuid.uuid4())
    chat_number = len(st.session_state.sessions) + 1

    st.session_state.sessions[new_id] = {
        "name": f"Chat {chat_number}",
        "chat_history": [],
        "sources": []
    }

    st.session_state.current_session = new_id

# ---------------- FILE UPLOAD ----------------
st.sidebar.markdown("---")
st.sidebar.title("📂 Upload Docs")

os.makedirs("data/raw_docs", exist_ok=True)

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF/DOCX",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        save_path = os.path.join("data/raw_docs", file.name)
        with open(save_path, "wb") as f:
            f.write(file.getbuffer())
    st.sidebar.success("Files uploaded!")

if st.sidebar.button("⚙️ Process Documents"):
    with st.spinner("Processing..."):
        requests.post(
            f"{API_URL}/ingest",
            params={"session_id": st.session_state.current_session}
        )


    st.sidebar.success("Done!")

# ---------------- CURRENT SESSION ----------------
session = st.session_state.sessions[st.session_state.current_session]

st.title(f"📄 Ask My Docs — {session['name']}")

# ---------------- CHAT INPUT ----------------
query = st.chat_input("Ask something...")

if query:
    session["chat_history"].append({
        "role": "user",
        "content": query
    })

    with st.spinner("Thinking..."):
        try:
            res = requests.post(
                f"{API_URL}/query",
                json={
                    "query": query,
                    "chat_history": session["chat_history"],
                    "session_id": st.session_state.current_session
                }
            )


            if res.status_code == 200:
                data = res.json()
            else:
                st.error(res.text)
                data = {"answer": "Error", "sources": []}

        except Exception as e:
            st.error(f"Backend error: {e}")
            data = {"answer": "Backend not running", "sources": []}



        data = res.json()

    answer = data.get("answer", "No response")
    sources = data.get("sources", [])

    session["chat_history"].append({
        "role": "assistant",
        "content": answer
    })

    session["sources"] = sources

# ---------------- DISPLAY CHAT ----------------
for i, msg in enumerate(session["chat_history"]):
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

        if msg["role"] == "assistant" and i == len(session["chat_history"]) - 1:
            if session["sources"]:
                with st.expander("📄 Sources"):
                    for src in session["sources"]:
                        st.markdown(f"""
                        **📄 Page:** {src.get("page", "N/A")}  
                        **📁 Source:** {src.get("source", "Unknown")}
                        """)
