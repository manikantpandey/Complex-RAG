import httpx
from app.core.config import settings

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {settings.groq_api_key}",
    "Content-Type": "application/json"
}

async def groq_chat(prompt: str) -> str:
    payload = {
        "model":settings.groq_model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_API_URL, json=payload, headers=HEADERS)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    
async def rewrite_question(question: str) -> str:
    prompt = f"Rewrite the following question to be clearer for a document search:\n\n{question}"
    return await groq_chat(prompt)
    
async def filter_context(chunks: list[str], question: str) -> str:
    joined_context = "\n\n".join(chunks)
    prompt = f"""Filter the relevant parts of this context to answer the question.\n\nQuestion: {question}\n\nContext:\n{joined_context}"""
    filtered = await groq_chat(prompt)
    return filtered.split("\n\n")

async def generate_answer(chunks: list[str], question: str) -> str:
    context = "\n\n".join(chunks)
    prompt = f"""Using the following context, answer the question:\n\nContext:\n{context}\n\nQuestion: {question}"""
    return await groq_chat(prompt)

async def evaluate_answer(answer: str, context: str) -> str:
    prompt = f"""Evaluate if the following answer is grounded and complete given the context.\n\nContext:\n{context}\n\nAnswer:\n{answer}"""
    response = await groq_chat(prompt)
    return {"faithfulness":"hallucinated" not in response.lower(), "completeness": "incomplete" not in response.lower()}

