from typing import Optional

from fastapi import APIRouter

from modules.Type import schemas
from modules.Type.schemas import TypeCreate, Type
from modules.Type.service import ProductService


router = APIRouter(prefix="/typeProduct", tags=["TypeProduct"])


@router.get("/", response_model=list[Type])
def list_typeProducts():
    service = ProductService()
    return service.get_products()
    # return service.get_products()


@router.get("/{id}/", response_model=Optional[Type])
def get_company_by_id(id: int):
    service = ProductService()
    return service.get_product_id(id)


@router.post("/", response_model=Type)
def add_company(typeProduct: TypeCreate):
    service = ProductService()
    return service.create_product(typeProduct)