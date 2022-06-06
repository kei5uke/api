from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World! This is my personal API!"}

@app.get("/whois/{name}")
async def introduction(name:str = Query(default=None, max_length=20)):
    if name == "keisuke":
        return {"name": "Keisuke K.", "passions": ["cybersecurity", "programming"]}

@app.get("/")
async def root():
    return {"message": "Hello World! This is my personal API!"}

