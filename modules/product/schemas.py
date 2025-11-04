from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str


class ProductCreate(BaseModel):
    name: str
