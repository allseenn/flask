# curl -X 'POST' 'http://127.0.0.1:8000/items/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "BestSale", "description": "The best of the best", "price": 9.99, "tax": 0.99}'
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "NewName", "description": "New description of the object", "price": 7.77, "tax": 10.01}'
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "NewName",  "price": 7.77}'
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "NewName"}'
# curl -X 'DELETE' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' 
import logging
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


items = {}


@app.get("/")
async def read_root():
    logger.info('Отработал GET-запрос')
    return {"Hello": "World"}


@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE {item_id}.')
    return {"item_id": item_id}