from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from extract import extract

app = FastAPI(title="ticket-extraction")


class EmailIn(BaseModel):
    email: str = Field(min_length=1, max_length=5000)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/extract")
async def extract_endpoint(body: EmailIn):
    try:
        ticket, attempts = await extract(body.email)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"extraction failed: {e}")
    return {"ticket": ticket.model_dump(), "attempts": attempts}
