baseline: valid 100%, category 87%, amount 97%, urgency(+-1) 57%
v6 (5th example: calm unauthorized debit, fraud/3/8500): urgency 23/30, category 26/30, amount 28/30. Worse than baseline 25/30 on golden_v3. Reverted to v4 prompt. Row-level diff not inspected.
Open: 5 over-escalation misses (rows 8,16,17,18,26) on "unauthorized"/"urgent"; amount None on rows 9, 13; category confusions (refund over-predicted).

## Week 2: prompt variants (30 emails, golden_v3)
| variant | valid | category | amount | urgency |
| bare | 30 | 25 | 30 | 15 |
| persona | 30 | 23 | 30 | 16 |
| rules | 30 | 27 | 30 | 21 |
| reasoning (all 5 keys named) | 30 | 26 | 29 | 22 |
| rules + 4 examples | 30 | 26 | 28 | 25 |
Findings: rules +6 urgency, examples +4 more, persona and reasoning = noise (reasoning also +30 tokens/call).
First reasoning run was invalid 17/30: model dropped required `summary`; Pydantic caught it. Retry with error text matters because temp 0 makes a blind retry identical.
Examples hurt amount: all 4 tie amount to "charged/debited", so rows 9 and 13 ("purchased for 150", "payment of 499") returned null. Untested fix: add an example with a purchase-price amount.
