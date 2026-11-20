from typing import Literal

from pydantic import BaseModel, Field


class Ticket(BaseModel):
    category: Literal["refund", "failed_payment", "fraud", "other"]
    urgency: int = Field(ge=1, le=5)
    amount: float | None = None
    summary: str
