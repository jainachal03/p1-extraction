import asyncio
import time

from openai import AsyncOpenAI
from pydantic import ValidationError

from schema import Ticket

llm = AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
MODEL = "qwen2.5:3b"

SYSTEM = """You are a support triage specialist at a payments company.
Read one customer email and return ONLY a JSON object with these fields:
- category: one of "refund", "failed_payment", "fraud", "other".
  fraud = the customer reports a debit they did not authorize.
  failed_payment = a payment failed or was declined, possibly with money still taken.
  refund = the customer asks for money back for a cancelled or returned purchase.
  other = anything else.
- urgency: integer from 1 to 5, the priority for the support team. Use the highest level that applies:
  5 = the customer mentions legal action, a chargeback, or a bank dispute (even as a possibility), or the email comes from a bank, regulator, or government agency.
  4 = the customer reports hardship, a long delay, strong anger, or a repeat contact, whatever the amount.
  3 = money is affected and the amount is 5000 rupees or more, with no complaint of hardship. Also use 3 if you cannot judge the urgency.
  2 = money is affected, the customer is calm, and the amount is below 5000 rupees.
  1 = a question or general message, no money affected.
  Words like "urgent" or "immediate" alone do not raise the level. The words "unauthorized", "wrongly charged" or "refund" describe the category, not the urgency. Raise the level only if one of the listed triggers appears.
- amount: the main amount in rupees as a number, or null if none is stated. Never guess.
- summary: one short sentence.
Rules:
- If the customer says a charge was unauthorized, the category is fraud, even if they also ask for money back.
- If an amount in rupees appears in the email, use it as the amount.
Return only the JSON, with no other text."""

EXAMPLES = [
    (
        "I did not enter any OTP for my phone purchase of 21000 but the money was still debited. It has been 7 days since I spoke to customer service and I am very disappointed.",
        '{"category": "fraud", "urgency": 4, "amount": 21000, "summary": "Customer reports an unauthorized debit of 21000 rupees and has waited 7 days."}',
    ),
    (
        "I was charged 1 rupee for a card verification but have not received the refund. Please take a look.",
        '{"category": "refund", "urgency": 2, "amount": 1, "summary": "Customer is waiting for a verification charge to be refunded."}',
    ),
    (
        "My card was declined twice at checkout but I was still charged 2,400 rupees. Fix this today or I will dispute it with my bank.",
        '{"category": "failed_payment", "urgency": 5, "amount": 2400, "summary": "Customer was charged 2400 rupees despite declined payments and threatens a bank dispute."}',
    ),
    (
        "My card payment of 7,500 rupees failed but the amount was still debited. Please check and reverse it.",
        '{"category": "failed_payment", "urgency": 3, "amount": 7500, "summary": "Customer was debited 7500 rupees for a failed payment."}',
    ),
]


def apply_rules(ticket):
    if ticket.urgency in (2, 3) and ticket.amount is not None:
        ticket.urgency = 3 if ticket.amount >= 5000 else 2
    return ticket


async def extract(email, max_attempts=2):
    messages = [{"role": "system", "content": SYSTEM}]
    for example_email, example_json in EXAMPLES:
        messages.append({"role": "user", "content": example_email})
        messages.append({"role": "assistant", "content": example_json})
    messages.append({"role": "user", "content": email})

    for attempt in range(1, max_attempts + 1):
        r = await llm.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0,
            max_tokens=200,
            response_format={"type": "json_object"},
        )
        text = r.choices[0].message.content
        try:
            return apply_rules(Ticket.model_validate_json(text)), attempt
        except ValidationError as err:
            problems = "\n".join(
                f"{'.'.join(str(p) for p in e['loc'])}: {e['msg']}" for e in err.errors()
            )
            messages.append({"role": "assistant", "content": text})
            messages.append({
                "role": "user",
                "content": f"Your reply failed validation:\n{problems}\nReturn the corrected JSON only.",
            })
    return None, max_attempts


if __name__ == "__main__":
    email = "I was supposed to get a 5% discount at the store with this card, but I was charged the full amount. Can you tell me why?"
    start = time.perf_counter()
    result, attempts = asyncio.run(extract(email))
    print(f"attempts={attempts} seconds={time.perf_counter() - start:.1f}")
    print(result)
