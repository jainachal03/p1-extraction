from pydantic import ValidationError

from schema import Ticket

good = '{"category": "fraud", "urgency": 8, "amount": 21000, "summary": "Unauthorized debit"}'
bad = '{"category": "payment issue", "urgency": 11, "amount": null, "summary": "Card declined"}'

print(Ticket.model_validate_json(good))
try:
    Ticket.model_validate_json(bad)
except ValidationError as e:
    print(e)
