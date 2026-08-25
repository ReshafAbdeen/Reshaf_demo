from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title="Item Management API")

# Pydantic Data Model for Request Body Validation
class Item(BaseModel):
    id: int
    name: str = Field(..., min_length=2, example="Laptop")
    price: float = Field(..., gt=0, example=50000.0)
    in_stock: bool = True

# In-Memory Database
db: List[Item] = []

@app.get("/items", response_model=List[Item])
def get_items():
    return db

@app.post("/items", status_code=201)
def add_item(item: Item):
    for existing_item in db:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item ID already exists!")
    db.append(item)
    return {"message": "Item added successfully!", "item": item}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found!")

# Note: Terminal me `uvicorn filename:app --reload` se run kiya jata hai.