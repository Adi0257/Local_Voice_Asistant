from sentence_transformers import CrossEncoder

reranker = CrossEncoder("BAAI/bge-reranker-base")


def rerank(query, docs, top_k=5):  # 🔥 increased
    pairs = [[query, doc.page_content] for doc in docs]
    scores = reranker.predict(pairs)

    ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)

    return [doc for doc, _ in ranked[:top_k]]
