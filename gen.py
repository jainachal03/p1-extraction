import asyncio
import itertools
import json
import random

from openai import AsyncOpenAI

llm = AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
random.seed(7)

SITUATIONS = {
    "fraud": "the customer sees a debit they say they never authorized",
    "failed_payment": "a payment failed or was declined, and money may still have been taken",
    "refund": "the customer is waiting for a refund for a cancelled or returned purchase",
    "other": "a general question or complaint that is not about fraud, a failed payment, or a refund",
}
URGENCY = {
    2: "calm, just asking, no money problem",
    4: "mildly worried, small amount or minor delay",
    6: "unhappy, believes they were charged wrongly, no deadline",
    8: "angry, money lost and waiting a long time",
    10: "furious, threatens legal action or a chargeback",
}

combos = list(itertools.product(SITUATIONS, URGENCY))
random.shuffle(combos)
combos = (combos + random.sample(combos, 10))[:30]


async def make(cat, urg):
    if cat == "other" and random.random() < 0.7:
        amount = None
    else:
        amount = random.choice([150, 499, 1200, 2400, 7000, 21000])
    amount_text = f"Mention the amount {amount} rupees." if amount else "Do not mention any amount."
    prompt = (
        "Write one realistic email, 2 to 4 sentences, from a customer to a payments company's support team. "
        f"Situation: {SITUATIONS[cat]}. Customer mood: {URGENCY[urg]}. {amount_text} "
        "Write only the email text, with no subject line, no name and no explanation."
    )
    r = await llm.chat.completions.create(
        model="qwen2.5:3b",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_tokens=150,
    )
    return {"email": r.choices[0].message.content.strip(), "category": cat, "urgency": urg, "amount": amount}


async def main():
    with open("golden_draft.jsonl", "w") as f:
        for i, (cat, urg) in enumerate(combos, 1):
            row = await make(cat, urg)
            f.write(json.dumps(row) + "\n")
            f.flush()
            print(i, cat, urg, flush=True)


asyncio.run(main())
