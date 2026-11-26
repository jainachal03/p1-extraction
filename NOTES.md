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

## Week 3: golden_v4 (100 emails, 25 per category, urgency mix 12/18/20/30/20)
First run on 100 (v4 prompt): valid 100, category 82, amount 92, urgency 82. Cache: 100 entries, 0 retries.
Failure taxonomy (36 miss lines):
A. general questions about refunds/payments/fraud routed to category other (6 rows: 31,32,49,50,67,68), label may be wrong
B. 'other' emails with money (cashback, bonus, fee, settlement) given urgency 1 and often amount None (86,87,88,89,92,95)
C. over-escalation of fraud 3/4 to 4/5 on 'unauthorized' (8,16,17,71,72,73,75,18,26)
D. category mix-ups: failed_payment->refund (56,61,62), fraud->other (74,77,80), fraud->refund (70)
E. under-escalation: sarcasm 45, bank dispute 83
F. amount None when money is not 'charged/debited' (9,13,33,86,87,89,95): confirms the Week 2 examples-narrowing hypothesis

Category rule (decided Nov 24): category follows the TOPIC of the email, including general questions
(a question about how refunds work is `refund`; about blocking a card is `fraud`; about retrying payments is `failed_payment`).
`other` = anything not about refunds, failed payments or fraud. An unauthorized charge is `fraud` even if the customer asks for money back.
Consequence: bucket A (6 rows) is a model error. Candidate fix: put this definition in SYSTEM and re-test.

## v9 (category/amount/urgency definitions added to SYSTEM) on golden_v4 (100)
valid 100, category 82, amount 96, urgency 83 (v7: 82/92/82).
Amount +4, 0 broken (clean win: positive definition, cashback/bonus/shipping rows fixed).
Urgency: 5 fixed, 4 broken (net +1, within churn); bucket B fixed 3 of 6.
Category: 2 fixed, 2 broken (all failed_payment); bucket A (general questions -> other) unchanged: prompt sentence does not override the model's prior.
New baseline for the pytest gate: category 82, amount 96, urgency 83 on 100.

## Multi-amount challenge set (golden_multi.jsonl, 9 emails; rule: amount = money the customer wants returned, separate figures summed)
category 9/9, amount 8/9, urgency 8/9. Only miss: row 7 (two cancelled orders 2,500 + 3,500 -> model returned None, urgency 2 instead of 3).
Cascade: amount None disables the 5,000 code rule, so one extraction error caused two wrong fields.
Idea (not built): schema returns amounts as a list and code sums them.
