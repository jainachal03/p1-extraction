ROWS_A = [
# ---------------- refund ----------------
("refund", 1, None, "", """Subject: Refund timeline question

Hi, how long does a refund usually take to reach my account after I cancel an order? Just want to know the general timeline.

Thanks"""),
("refund", 1, None, "", """Subject: Where do refunds go?

Do refunds go back to the original payment method or to my wallet? I am asking before I place an order."""),
("refund", 2, 350, "", """Subject: Shipping charge on returned item

Hi Support,

I returned a pair of earphones (order 4471) and was still charged 350 rupees for shipping, although the return policy says returns are free. Could you refund the shipping amount?

Thanks"""),
("refund", 2, 1200, "", """Subject: Trial cancellation refund

I cancelled my gym subscription inside the trial period but 1,200 rupees was still taken. Please refund it when you can."""),
("refund", 2, 4999, "boundary: just below 5000", """Subject: Annual plan cancelled same day

I was billed Rs. 4,999 for an annual plan that I cancelled the same day. Kindly process the refund. No rush."""),
("refund", 3, 5000, "boundary: exactly 5000 (rule is >=5000)", """Subject: Cancelled order refund

My order of 5000 rupees was cancelled by the seller yesterday and the money has not come back to my account yet. Could you check the status and refund it?"""),
("refund", 3, 5001, "boundary: just above 5000", """Subject: Flight cancellation refund

I paid 5,001 rupees for a flight booking that the airline cancelled. Please refund the amount to my account."""),
("refund", 3, 18500, "", """Subject: Refund for cancelled furniture order

Please process a refund of Rs. 18,500 for the cancelled furniture order. The seller confirmed the cancellation yesterday.

Regards"""),
("refund", 3, 9200, "amount not phrased as charged/debited", """Subject: Return pickup done, refund pending

I returned a laptop bag that cost ₹9,200 and the pickup was completed today. Kindly initiate the refund and let me know when to expect it."""),
("refund", 4, 2300, "repeat contact", """Subject: Third email about my refund

This is my third email about the 2,300 rupee refund for a damaged phone cover. Nobody has replied. Please look at this today."""),
("refund", 4, 800, "hardship", """Subject: Refund for cancelled order

The 800 rupees from my cancelled order has not been refunded, and it was the money I had set aside for this week's groceries. It is a real struggle for me right now. Please refund it soon."""),
("refund", 4, 15000, "strong anger + long delay", """Subject: Unacceptable service

I am absolutely furious. You promised the 15,000 rupee refund within 5 days. It has been 25 days and your team keeps giving me excuses. This is unacceptable."""),
("refund", 4, None, "long delay, no amount", """Subject: Refund still pending

I cancelled my subscription in September and the refund still has not arrived. It has been over two months now. Please tell me what is going on."""),
("refund", 4, 3999, "repeat contact", """Subject: Refund of Rs. 3,999

I called twice and wrote once already about my refund of Rs. 3,999 and still nothing. I am really disappointed with how this is being handled."""),
("refund", 4, 450, "sarcasm; label = anger + long delay", """Subject: Great service

Wow, amazing service. Thirty days to refund a 450 rupee order, truly world class. I am fed up. Is the money coming back before the end of the year?"""),
("refund", 5, 6000, "chargeback", """Subject: Last chance

If my refund of 6,000 rupees is not credited by Friday I will raise a chargeback with my bank."""),
("refund", 5, 2500, "legal", """Subject: Legal notice

I am consulting a lawyer about the 2,500 rupees you owe me as a refund. A legal notice will follow if I do not hear from you within a week."""),
("refund", 5, None, "legal (consumer court)", """Subject: Final warning

This is my final warning. I will file a case in the consumer court over my pending refund unless it is resolved."""),
# ---------------- failed_payment ----------------
("failed_payment", 1, None, "", """Subject: Question about failed payments

What should I do if my UPI payment fails but I see a pending message? Is there a standard time after which the amount is reversed?"""),
("failed_payment", 1, None, "", """Subject: Retry limit

Is there a limit on how many times a payment can be retried before the card is blocked? Just curious."""),
("failed_payment", 2, 600, "", """Subject: Recharge failed

My payment of 600 rupees for a mobile recharge failed but the amount was debited. Please reverse it."""),
("failed_payment", 2, 1850, "", """Subject: Merchant payment shows failed

A payment to a merchant for ₹1,850 shows failed in the app but my bank statement shows a debit. Could you check?"""),
("failed_payment", 2, 3200, "amount not phrased as charged/debited", """Subject: Checkout error

The order total of 3200 rupees did not go through at checkout, though I got an SMS saying the money left my account. Please look into this when possible."""),
("failed_payment", 3, 12000, "", """Subject: Failed payment, money deducted

My card payment of 12,000 rupees failed at checkout but the amount was debited from my account. Please reverse it."""),
("failed_payment", 3, 7800, "", """Subject: Electricity bill payment

A transaction of Rs. 7,800 to the electricity board failed but I received a debit alert. Could you confirm whether it will be reversed?"""),
("failed_payment", 3, 25000, "", """Subject: Tuition fee payment

I tried to pay a 25,000 rupee tuition fee. The app said payment failed, yet my balance dropped. Please check and revert."""),
("failed_payment", 3, 5200, "", """Subject: Bill payment error

My bill payment of 5,200 rupees shows as failed but the money was taken from my account. Kindly check and reverse it."""),
("failed_payment", 4, 4500, "hardship", """Subject: Rent payment failed

My rent payment of 4,500 rupees failed but the money was deducted, and now my landlord is threatening to evict me. I have no other funds this month. Please help."""),
("failed_payment", 4, None, "repeat contact, no amount", """Subject: Second email

Second email about this. My payment failed last Tuesday and I have been charged. I have contacted support twice already with no reply."""),
("failed_payment", 4, 22000, "strong anger", """Subject: Where is my money

This is ridiculous. 22,000 rupees debited for a failed payment and nobody can tell me where the money is. I am extremely angry with this service."""),
("failed_payment", 4, 950, "long delay", """Subject: Reversal overdue

The 950 rupees from my failed payment has not been reversed in 21 days. Your help page says 5 to 7 working days. Please escalate."""),
("failed_payment", 4, 6500, "hardship", """Subject: Please return my money

I am a daily wage worker and the 6,500 rupees stuck after a failed payment is my entire month's savings. Please return it quickly, I cannot manage without it."""),
("failed_payment", 4, 1500, "sarcasm; repeat issue + anger", """Subject: Great job again

Great job again. My payment of 1500 rupees failed, the money vanished, and the app says everything is fine. This is the third time this month, thanks for nothing."""),
("failed_payment", 5, 3000, "chargeback", """Subject: Failed payment, chargeback

My 3,000 rupee payment failed but was debited. I have already asked my bank to raise a chargeback and will go ahead unless you reverse it today."""),
("failed_payment", 5, None, "from a bank", """Subject: Grievance cell notice

From the Grievance Cell, ABC Bank: Our customer reports that a failed transaction on your platform was debited and not reversed. Please confirm the status within 3 working days as per the RBI turnaround rules."""),
("failed_payment", 5, 14000, "legal", """Subject: Legal action

I will be taking legal action if the 14,000 rupees from my failed payment is not returned. My advocate has the transaction details."""),
]
