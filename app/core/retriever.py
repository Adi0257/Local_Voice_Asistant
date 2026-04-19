from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.retrievers import BM25Retriever

import pickle
import os

CHROMA_PATH = "data/chroma"
PROCESSED_PATH = "data/processed"


def load_retrievers(session_id):
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en")

    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
        collection_name=f"rag_{session_id}"
    )

    chunk_path = os.path.join(PROCESSED_PATH, f"chunks_{session_id}.pkl")

    if os.path.exists(chunk_path):
        with open(chunk_path, "rb") as f:
            chunks = pickle.load(f)
        bm25 = BM25Retriever.from_documents(chunks)
        bm25.k = 5
    else:
        bm25 = BM25Retriever.from_documents([])

    return vectorstore, bm25


def hybrid_retrieve(query, vectorstore, bm25):
    bm25_docs = bm25.invoke(query)
    vector_docs = vectorstore.similarity_search(query, k=10)  # 🔥 more recall

    combined = bm25_docs + vector_docs

    # remove duplicates
    unique = {doc.page_content: doc for doc in combined}

    return list(unique.values())
