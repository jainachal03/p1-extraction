import asyncio, json
from extract import extract

# Minimum correct counts out of 30 on golden_v3 (the v4 baseline)
BASELINE = {"category": 82, "amount": 96, "urgency": 83}

def test_accuracy_not_below_baseline():
    gold = [json.loads(l) for l in open("golden_v4.jsonl")]

    async def run():
        hits = {"category": 0, "amount": 0, "urgency": 0}
        for g in gold:
            try:
                t, _ = await extract(g["email"])
            except Exception:
                continue
            hits["category"] += t.category == g["category"]
            hits["urgency"] += t.urgency == g["urgency"]
            a, b = t.amount, g["amount"]
            hits["amount"] += (a is None and b is None) or (
                a is not None and b is not None and float(a) == float(b))
        return hits

    hits = asyncio.run(run())
    for field, minimum in BASELINE.items():
        assert hits[field] >= minimum, f"{field}: {hits[field]} < baseline {minimum}"
