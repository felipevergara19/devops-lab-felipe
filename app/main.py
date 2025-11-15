from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/items")
def create_item(item: Item):
    return {"message": "Item created", "item": item}
