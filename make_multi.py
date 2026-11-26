import json
ROWS = [
("fraud", 2, 2500, "distractor: wallet balance is not the disputed amount", """Subject: Unauthorized debit

Hi Support,

My wallet had 40,000 rupees yesterday and a debit of 2,500 rupees went out that I did not make. Could you look into it?

Thanks"""),
("refund", 3, 5000, "partial refund: three figures, wanted = remaining 5,000", """Subject: Partial refund received

I paid 8,000 rupees for an order that I returned. You refunded only 3,000 rupees. Please send the remaining 5,000 rupees."""),
("fraud", 2, 2100, "sum rule: list of three unauthorized debits", """Subject: Three debits I did not make

I see three debits on my account that I did not authorise: 500 rupees, 700 rupees and 900 rupees. Please investigate and return the money."""),
("failed_payment", 2, 3000, "sum rule: same amount twice, both debited", """Subject: Payment failed twice

My payment of 1,500 rupees failed. I retried and the retry of 1,500 rupees also failed, but both amounts were debited from my account. Please reverse both."""),
("refund", 2, 1500, "wanted = remaining delivery fee, not the order total", """Subject: Delivery fee not refunded

The order total was 12,500 rupees including 1,500 rupees delivery. I returned the order and you refunded 11,000 rupees. The delivery fee of 1,500 rupees should come back too."""),
("refund", 2, 500, "needs arithmetic: 999 charged vs 499 advertised", """Subject: Charged more than the listed price

I was charged 999 rupees for a plan that your website lists at 499 rupees. Please refund the difference."""),
("refund", 3, 6000, "sum crosses the 5000 threshold, so urgency 3", """Subject: Two cancelled orders

I cancelled two orders, one for 2,500 rupees and one for 3,500 rupees. Neither amount has been refunded yet. Could you process both?"""),
("fraud", 2, 4000, "same figure in digits and words: do not sum", """Subject: Debit of 4,000

A debit of Rs. 4,000 (four thousand rupees) was made from my account without my approval. Please check and reverse it."""),
("other", 1, None, "past figure, nothing to return", """Subject: Statement request

Last month I was charged 800 rupees and you already refunded it, thank you. I only need a statement for that month for my records. How can I download it?"""),
]
with open("golden_multi.jsonl", "w") as f:
    for cat, urg, amt, note, email in ROWS:
        f.write(json.dumps({"email": email.strip(), "category": cat, "urgency": urg, "amount": amt, "note": note}) + "\n")
print(len(ROWS), "rows written")
