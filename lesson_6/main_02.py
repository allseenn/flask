from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(max_length=10)

class User(BaseModel):
    age: int = Field(default=0)

