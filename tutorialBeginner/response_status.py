from fastapi import FastAPI

app = FastAPI()

# The status_code parameter receives a number with the HTTP status code.
@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}