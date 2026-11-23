import hashlib, json, sqlite3
import openai
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

TIMEOUT = 90  # seconds per attempt

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((openai.APITimeoutError, openai.APIConnectionError)),
    reraise=True,
)
async def _call(llm, **params):
    return await llm.chat.completions.create(timeout=TIMEOUT, **params)


db = sqlite3.connect("llm_cache.db")
db.execute("CREATE TABLE IF NOT EXISTS c (k TEXT PRIMARY KEY, v TEXT)")

async def cached_chat(llm, **params):
    key = hashlib.sha256(json.dumps(params, sort_keys=True).encode()).hexdigest()
    row = db.execute("SELECT v FROM c WHERE k=?", (key,)).fetchone()
    if row:
        return row[0]
    r = await _call(llm, **params)
    text = r.choices[0].message.content
    db.execute("INSERT OR REPLACE INTO c VALUES (?,?)", (key, text))
    db.commit()
    return text
