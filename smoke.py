from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
reply = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[{"role": "user", "content": "Reply with exactly one word: OK"}],
)
print(reply.choices[0].message.content)
print(reply.usage)
