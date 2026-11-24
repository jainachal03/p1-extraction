ROWS_B = [
# ---------------- fraud ----------------
("fraud", 1, None, "contains 'unauthorized' but is only a question", """Subject: Blocking my card

How do I block my card or UPI ID if I think someone else might get access to it? Just want to be prepared."""),
("fraud", 1, None, "contains 'unauthorized' but is only a question", """Subject: Alerts

Does the app send an alert for every debit? I want to spot unauthorized transactions early."""),
("fraud", 2, 750, "", """Subject: Debit I do not recognise

I see a debit of 750 rupees to a merchant I do not recognise. I did not make this payment. Could you look into it?"""),
("fraud", 2, 1999, "unauthorized charge, asks money back: still fraud", """Subject: Subscription I never signed up for

There is a Rs. 1,999 subscription charge on my account that I never signed up for. Please cancel it and refund the money."""),
("fraud", 3, 11000, "", """Subject: Unknown transfer

A transfer of 11,000 rupees left my account yesterday to a name I do not know. I did not authorise it. Please investigate."""),
("fraud", 3, 6000, "", """Subject: Debit I did not make

I noticed a ₹6,000 debit that I did not make. I have not shared my PIN or OTP with anyone. Kindly look into it."""),
("fraud", 3, 40000, "", """Subject: Payment I never approved

Hello, 40,000 rupees were debited through a payment I never approved. Please let me know what the next steps are."""),
("fraud", 3, 5500, "amount not phrased as charged/debited", """Subject: Unknown purchase

An online purchase of 5,500 rupees appeared on my statement. I did not buy anything from this site. Could you check?"""),
("fraud", 4, 9000, "hardship", """Subject: Money taken from my account

Someone drained 9,000 rupees from my account without my permission, and I cannot pay my medical bills this week because of it. I need this fixed urgently."""),
("fraud", 4, None, "repeat contact, no amount", """Subject: Reported twice already

I have reported the unauthorized transaction on my account two times already and heard nothing. Please respond this time."""),
("fraud", 4, 30000, "strong anger", """Subject: Disgraceful

I am livid. 30,000 rupees disappeared from my wallet and nobody at your company seems to care. This is a disgrace."""),
("fraud", 4, 2700, "long delay", """Subject: Investigation status

I reported an unauthorised debit of 2,700 rupees 18 days ago and I have not heard anything since. How long does an investigation take?"""),
("fraud", 4, 12500, "repeat contact", """Subject: Follow up on my complaint

Following up on my earlier complaint ticket about the 12,500 rupee unauthorized payment. This is my fourth message."""),
("fraud", 4, 3500, "hardship", """Subject: Phone stolen

My phone was stolen and 3,500 rupees were spent through the app. I am a student and this was my fees money. Please help me."""),
("fraud", 5, 16000, "legal (FIR)", """Subject: Unauthorized debit

Unauthorized debit of 16,000 rupees. If this is not resolved I will file an FIR and a complaint with the cyber crime cell."""),
("fraud", 5, None, "from a regulator", """Subject: Complaint registered

From: Office of the Banking Ombudsman. A complaint has been registered against your service regarding unauthorized debits. You are required to submit your response within 15 days."""),
("fraud", 5, 7200, "bank dispute", """Subject: Disputing this payment

I did not authorise the 7,200 rupee payment and I am disputing it with my bank today."""),
# ---------------- other ----------------
("other", 1, None, "", """Subject: Update mobile number

How do I update the mobile number linked to my account?"""),
("other", 1, None, "", """Subject: Statement download

Can you share the steps to download my monthly statement as a PDF?"""),
("other", 2, 300, "", """Subject: Cashback missing

The 300 rupees cashback promised for my first transaction has not shown up in my wallet. The offer was valid till last month. Could you check?"""),
("other", 2, 899, "LOW CONFIDENCE: category could be refund", """Subject: Annual fee

I was charged a Rs. 899 annual fee on my card, but I thought the first year was free. Could you clarify?"""),
("other", 3, 8000, "", """Subject: Merchant settlement pending

Our merchant settlement of 8,000 rupees for last Friday's sales has not been credited yet. Please let me know when it will arrive."""),
("other", 3, 6500, "", """Subject: Festival cashback

My cashback reward of 6,500 rupees from the festival campaign is still not in my wallet. Could you check the status?"""),
("other", 3, 15000, "LOW CONFIDENCE: money affected but category fuzzy", """Subject: Voucher expired because of a bug

My cashback voucher worth 15,000 rupees expired before it could be activated because of the app bug. Please restore it."""),
("other", 4, None, "repeat contact", """Subject: Account locked

This is my fifth message about my account being locked. I cannot access my funds and nobody is replying."""),
("other", 4, 500, "sarcasm; anger", """Subject: Fantastic

Fantastic, your app crashed again during my 500 rupee payment. I am so tired of this broken app. Do something about it."""),
("other", 4, None, "hardship", """Subject: Account frozen

My account has been frozen for 3 weeks. I run a small shop and cannot pay my suppliers. This is hurting my business badly. Please help me."""),
("other", 4, None, "Hinglish; anger + delay", """Subject: Account band hai

Bhai, kya chal raha hai? Mera account teen din se band hai aur koi reply nahi de raha. Bahut gussa aa raha hai, jaldi theek karo."""),
("other", 4, 2000, "repeat contact", """Subject: Welcome bonus

Second time writing. The promised 2,000 rupee welcome bonus is still missing and your chat support just closes my tickets."""),
("other", 5, None, "from government", """Subject: Notice

From: Department of Consumer Affairs, Government of Telangana. A complaint has been filed against your company. Please respond with your grievance redressal officer's details within 7 days."""),
("other", 5, None, "from a bank", """Subject: Compliance request

This is the compliance team at XYZ Bank. We need confirmation of the merchant account details linked to the settlement dispute raised by our customer."""),
("other", 5, None, "legal", """Subject: Legal notice

My lawyer will be sending a legal notice over the repeated deletion of my account data without consent. Please acknowledge this email."""),
("other", 5, None, "legal (consumer court)", """Subject: Misleading offer

I will take your company to consumer court over the misleading cashback advertisement. Please share who I should address the case to."""),
("other", 5, None, "legal (complaint to regulator + proceedings)", """Subject: Data deletion request

Under the Digital Personal Data Protection Act I request deletion of all my data. Non-compliance will lead to a complaint to the Data Protection Board and legal proceedings."""),
]
