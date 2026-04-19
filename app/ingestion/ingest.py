from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from chromadb import Client
from chromadb.config import Settings

import os
import uuid
import pickle

CHROMA_PATH = "data/chroma"
RAW_PATH = "data/raw_docs"
PROCESSED_PATH = "data/processed"


def clear_collection(session_id):
    client = Client(Settings(persist_directory=CHROMA_PATH))
    collection_name = f"rag_{session_id}"

    try:
        client.delete_collection(name=collection_name)
        print(f"🧹 Cleared old collection: {collection_name}")
    except:
        pass


def ingest_docs(session_id):
    clear_collection(session_id)

    all_chunks = []

    for file in os.listdir(RAW_PATH):
        path = os.path.join(RAW_PATH, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
        elif file.endswith(".docx"):
            loader = Docx2txtLoader(path)
        else:
            continue

        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150,
            separators=["\n\n", "\n", ".", " "]
        )

        chunks = splitter.split_documents(docs)

        for i, chunk in enumerate(chunks):
            chunk.metadata.update({
                "doc_id": session_id,
                "chunk_id": i,
                "source": file,
                "page": chunk.metadata.get("page", 0)
            })

        all_chunks.extend(chunks)

    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en")

    vectorstore = Chroma.from_documents(
        documents=all_chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
        collection_name=f"rag_{session_id}"
    )

    os.makedirs(PROCESSED_PATH, exist_ok=True)

    with open(os.path.join(PROCESSED_PATH, f"chunks_{session_id}.pkl"), "wb") as f:
        pickle.dump(all_chunks, f)

    print(f"✅ Ingestion complete for session {session_id}")
