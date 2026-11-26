import asyncio, json, random, statistics, time
from extract import llm, MODEL, SYSTEM, EXAMPLES

gold = [json.loads(l) for l in open("golden_v4.jsonl")]
random.seed(1)
sample = random.sample(gold, 30)

def pct(values, q):
    v = sorted(values)
    return v[min(len(v) - 1, round(q * (len(v) - 1)))]

async def main():
    secs, ptok, ctok = [], [], []
    for g in sample:
        msgs = [{"role": "system", "content": SYSTEM}]
        for e, j in EXAMPLES:
            msgs += [{"role": "user", "content": e}, {"role": "assistant", "content": j}]
        msgs.append({"role": "user", "content": g["email"]})
        t = time.perf_counter()
        r = await llm.chat.completions.create(
            model=MODEL, messages=msgs, temperature=0, max_tokens=200,
            response_format={"type": "json_object"})
        secs.append(time.perf_counter() - t)
        ptok.append(r.usage.prompt_tokens)
        ctok.append(r.usage.completion_tokens)
        print(len(secs), round(secs[-1], 1), flush=True)
    print(f"\nlatency seconds: p50 {pct(secs, .5):.1f}  p95 {pct(secs, .95):.1f}  max {max(secs):.1f}  mean {statistics.mean(secs):.1f}")
    print(f"tokens per call: prompt {statistics.mean(ptok):.0f}  completion {statistics.mean(ctok):.0f}")
    print(f"total tokens for {len(secs)} calls: {sum(ptok) + sum(ctok)}")

asyncio.run(main())
