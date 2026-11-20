baseline: valid 100%, category 87%, amount 97%, urgency(+-1) 57%
v6 (5th example: calm unauthorized debit, fraud/3/8500): urgency 23/30, category 26/30, amount 28/30. Worse than baseline 25/30 on golden_v3. Reverted to v4 prompt. Row-level diff not inspected.
Open: 5 over-escalation misses (rows 8,16,17,18,26) on "unauthorized"/"urgent"; amount None on rows 9, 13; category confusions (refund over-predicted).
