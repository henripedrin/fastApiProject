from typing import Optional, List

from fastapi import APIRouter, HTTPException

from modules.product import schemas, service
from modules.product.schemas import ProductCreate, Product
from modules.product.service import ProductService


# from app.modules.company import service, schemas

router = APIRouter(prefix="/product", tags=["Product"])


@router.get("/", response_model=list[schemas.Product])
def list_products():
    service = ProductService()
    return service.get_products()
    # return service.get_companies()


@router.get("/{id}/", response_model=Optional[schemas.Product])
def get_product_by_id(id: int):
    service = ProductService()
    return service.get_product_id(id)



@router.post("/", response_model=schemas.Product)
def add_product(product: ProductCreate):
    service = ProductService()
    return service.create_product(product)


@router.get("/{empresa_id}/produtos", response_model=List[Product])
def list_produtos_by_empresa(empresa_id: int):
    produtos = service.get_produtos_by_empresa(empresa_id)

    if produtos is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Empresa com ID {empresa_id} não encontrada.")

    return produtos