import asyncio
import json
import sys

from extract import extract

TAG = sys.argv[1] if len(sys.argv) > 1 else "run"
PATH = sys.argv[2] if len(sys.argv) > 2 else "golden_v2.jsonl"


def score(pred, row):
    if pred is None:
        return {"valid": 0, "category": 0, "amount": 0, "urgency": 0}
    return {
        "valid": 1,
        "category": int(pred.category == row["category"]),
        "amount": int(pred.amount == row["amount"]),
        "urgency": int(pred.urgency == row["urgency"]),
    }


async def main():
    rows = [json.loads(line) for line in open(PATH)]
    totals = {"valid": 0, "category": 0, "amount": 0, "urgency": 0}
    retries = 0
    saved = []
    for i, row in enumerate(rows, 1):
        pred, attempts = await extract(row["email"])
        retries += attempts - 1
        s = score(pred, row)
        for k, v in s.items():
            totals[k] += v
        saved.append({
            "row": i,
            "label": {k: row[k] for k in ("category", "urgency", "amount")},
            "pred": pred.model_dump() if pred else None,
            "score": s,
        })
        print(i, s, flush=True)
    with open(f"results_{TAG}.json", "w") as f:
        json.dump(saved, f, indent=1)
    n = len(rows)
    print()
    for k, v in totals.items():
        print(f"{k}: {v}/{n} = {v / n:.0%}")
    print("retries used:", retries)
    print()
    for r in saved:
        if not all(r["score"].values()):
            L, P = r["label"], r["pred"]
            got = f"{P['category']}/{P['urgency']}/{P['amount']}" if P else "invalid"
            print(f"[{r['row']}] expected {L['category']}/{L['urgency']}/{L['amount']}  got {got}")


asyncio.run(main())
