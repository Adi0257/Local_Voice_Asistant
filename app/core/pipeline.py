from app.core.retriever import load_retrievers, hybrid_retrieve
from app.core.reranker import rerank
from app.core.generator import generate_answer


def run_pipeline(query, chat_history, session_id):
    vectorstore, bm25 = load_retrievers(session_id)

    docs = hybrid_retrieve(query, vectorstore, bm25)
    reranked_docs = rerank(query, docs)

    answer = generate_answer(query, reranked_docs, chat_history)

    return {
        "answer": answer,
        "sources": [
            {
                "page": doc.metadata.get("page"),
                "source": doc.metadata.get("source")
            }
            for doc in reranked_docs
        ]
    }
