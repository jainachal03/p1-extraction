import asyncio, json, sys
from extract import llm, MODEL, SYSTEM, apply_rules
from schema import Ticket

FIELDS = ('Return only JSON with keys: category (refund, failed_payment, fraud, other), '
          'urgency (integer 1-5), amount (number in rupees or null), summary (one sentence).')
PERSONA = "You are a veteran customer-support triage lead with 15 years of experience. "
REASON = ' Return the keys in this order: reasoning (one sentence), category, urgency, amount, summary.'

VARIANTS = {
    "bare": (FIELDS, 200),
    "persona": (PERSONA + FIELDS, 200),
    "rules": (SYSTEM, 200),
    "reasoning": (SYSTEM + REASON, 300),
}

async def run(name):
    system, max_tokens = VARIANTS[name]
    gold = [json.loads(l) for l in open("golden_v3.jsonl")]
    valid = cat = amt = urg = 0
    out = []
    for i, g in enumerate(gold, 1):
        r = await llm.chat.completions.create(
            model=MODEL,
            messages=[{"role": "system", "content": system},
                      {"role": "user", "content": g["email"]}],
            temperature=0, max_tokens=max_tokens,
            response_format={"type": "json_object"})
        try:
            t = apply_rules(Ticket.model_validate_json(r.choices[0].message.content))
        except Exception:
            out.append({"row": i, "pred": None}); continue
        valid += 1
        cat += t.category == g["category"]
        amt += (t.amount == g["amount"]) or (t.amount is not None and g["amount"] is not None and float(t.amount) == float(g["amount"]))
        urg += t.urgency == g["urgency"]
        out.append({"row": i, "pred": t.model_dump()})
        print(i, end=" ", flush=True)
    json.dump(out, open(f"results_cmp_{name}.json", "w"))
    n = len(gold)
    print(f"\n{name}: valid {valid}/{n}  category {cat}/{n}  amount {amt}/{n}  urgency {urg}/{n}")

async def main():
    for v in sys.argv[1:]:
        await run(v)

asyncio.run(main())
