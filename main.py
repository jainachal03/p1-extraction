import json
import time

from fastapi import FastAPI
from openai import AsyncOpenAI

app = FastAPI()
llm = AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="ollama")


@app.post("/chat")
async def chat(q: str, temperature: float = 0.7):
    start = time.perf_counter()
    r = await llm.chat.completions.create(
        model="qwen2.5:3b",
        messages=[{"role": "user", "content": q + " Answer in two sentences."}],
        temperature=temperature,
        max_tokens=100,
    )
    seconds = round(time.perf_counter() - start, 2)
    record = {
        "temperature": temperature,
        "prompt_tokens": r.usage.prompt_tokens,
        "completion_tokens": r.usage.completion_tokens,
        "seconds": seconds,
    }
    with open("calls.jsonl", "a") as f:
        f.write(json.dumps(record) + "\n")
    return {"answer": r.choices[0].message.content, **record}
