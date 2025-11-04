from pydantic import BaseModel

class Supplier(BaseModel):
    id: int
    name: str

class SupplierCreate(BaseModel):
    name: str
