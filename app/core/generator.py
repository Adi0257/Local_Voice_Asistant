from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model_name="openai/gpt-oss-20b",  # fast + cheap
    api_key="York-Groq-Key"
)

PROMPT = """
You are a strict document QA assistant.

Rules:
- Answer ONLY using the provided context
- Do NOT guess or hallucinate
- If answer is not clearly present → say "I don't know"
- Extract exact names, companies, values from text

Chat History:
{history}

Context:
{context}

Question:
{question}

Answer:
"""


def format_history(chat_history):
    formatted = ""
    for msg in chat_history[-5:]:
        formatted += f"{msg['role']}: {msg['content']}\n"
    return formatted


def generate_answer(query, docs, chat_history):
    context = "\n\n".join([
        f"[{i}] {doc.page_content}" for i, doc in enumerate(docs)
    ])

    history = format_history(chat_history)

    prompt = PROMPT.format(
        history=history,
        context=context,
        question=query
    )

    response = llm.invoke(prompt)

    return response.content
