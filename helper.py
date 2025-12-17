


def add_month(user_id: str, year: int, month: str):
    key = f"user:{user_id}:monaten"
    r.sadd(key, f"{year}_{month}")

def remove_month(user_id: str, year: int, month: str):
    key = f"user:{user_id}:monaten"
    r.srem(key, f"{year}_{month}")

def get_months(user_id: str):
    key = f"user:{user_id}:monaten"
    raw = r.smembers(key)
    return [{"year": int(x.split("_",1)[0]), "month": x.split("_",1)[1]} for x in raw]

def set_text(user_id: str, text: str):
    r.set(f"user:{user_id}:text", text)

def get_text(user_id: str):
    return r.get(f"user:{user_id}:text")