import json
import sys
from collections import Counter

rows = json.load(open(f"results_{sys.argv[1]}.json"))
conf = Counter()
cat = Counter()
for r in rows:
    if r["pred"] is None:
        continue
    conf[(r["label"]["urgency"], r["pred"]["urgency"])] += 1
    if r["label"]["category"] != r["pred"]["category"]:
        cat[(r["label"]["category"], r["pred"]["category"])] += 1

print("urgency: rows = your label, columns = model's pick")
print("      " + "  ".join(str(c) for c in range(1, 6)))
for a in range(1, 6):
    print(f"  {a}:  " + "  ".join(str(conf[(a, b)]) for b in range(1, 6)))
print()
print("category confusions (label -> model):")
for (a, b), n in cat.items():
    print(f"  {a} -> {b}: {n}")
print()
print("amount misses:")
for r in rows:
    if r["pred"] and r["label"]["amount"] != r["pred"]["amount"]:
        print(f"  [{r['row']}] label {r['label']['amount']}  model {r['pred']['amount']}")
