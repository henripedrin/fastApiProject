from modules.stock.repository import StockRepository
from modules.stock.schemas import StockCreate


class StockService:
    def get_stocks(self):
        repository = StockRepository()
        return repository.get_all()

    def create_stock(self, stock: StockCreate):
        if not stock.name or stock.name.strip() == "":
            raise ValueError("O nome é obrigatório")
        if len(stock.name) > 255:
            raise ValueError("O nome grande demais")

        repository = StockRepository()
        existing = stock.get_id()
        if existing:
            raise ValueError("Estoque já existe")

        return repository.save(stock)

    def get_stock_id(self, id: int):
        repository = StockRepository()
        stock = repository.get_id(id)
        return stock