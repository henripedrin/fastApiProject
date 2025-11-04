from typing import Optional

from fastapi import APIRouter

from modules.stock.schemas import Stock, StockCreate
from modules.stock.service import StockService

router = APIRouter(prefix="stock", tags=["Stock"])

@router.get("/",  response_model=list[Stock])
def list_stocks():
    service = StockService()
    return  service.get_stocks()

@router.get("/{id}/", response_model=Optional[Stock])
def get_stock_by_id(id: int):
    service = StockService()
    return service.get_stock_id()

@router.get("/", response_model=Stock)
def get_stock_by_company(id: int):
    service = StockService
    return service.get_stock_id()


@router.post("/", response_model=Stock)
def add_stock(stock: StockCreate):
    service = StockService
    return service.create_stock(stock)

