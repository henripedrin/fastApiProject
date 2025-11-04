from pydantic import BaseModel

class Stock(BaseModel):
    id: int
    name: str

class StockCreate(BaseModel):
    name: str