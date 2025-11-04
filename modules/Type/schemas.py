from pydantic import BaseModel

class Type(BaseModel):
    id: int
    name: str

class TypeCreate(BaseModel):
    name: str
