import hashlib, json, sqlite3

db = sqlite3.connect("llm_cache.db")
db.execute("CREATE TABLE IF NOT EXISTS c (k TEXT PRIMARY KEY, v TEXT)")

async def cached_chat(llm, **params):
    key = hashlib.sha256(json.dumps(params, sort_keys=True).encode()).hexdigest()
    row = db.execute("SELECT v FROM c WHERE k=?", (key,)).fetchone()
    if row:
        return row[0]
    r = await llm.chat.completions.create(**params)
    text = r.choices[0].message.content
    db.execute("INSERT OR REPLACE INTO c VALUES (?,?)", (key, text))
    db.commit()
    return text
