from typing import Optional

from fastapi import APIRouter

from modules.supplier.schemas import Supplier, SupplierCreate
from modules.supplier.service import SupplierService

router = APIRouter(prefix="/supplier", tags=["Supplier"])


@router.get("/", response_model=list[Supplier])
def list_suppliers():
    service = SupplierService()
    return service.get_suppliers()


@router.get("/{id}", response_model=Optional[Supplier])
def get_supplier_by_id(id: int):
    service = SupplierService()
    return service.get_supplier_id(id)


@router.post("/", response_model=Supplier)
def add_supplier(supplier: SupplierCreate):
    service = SupplierService()
    return service.create_supplier(supplier)
