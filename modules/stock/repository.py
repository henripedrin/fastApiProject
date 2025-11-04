from core.db import DataBase
from modules.stock.schemas import StockCreate


class StockRepository:
    QUERY_STOCKS = "SELECT id, name FROM stock"
    QUERY_STOCKS_ID = "SELECT id, name FROM stock where id = %s"
    QUERY_CREATE_STOCK = "INSERT INTO stock (name) VALUES ($s) RETURNING id;"

    def get_all(self):
        db = DataBase()
        stocks = db.execute(self.QUERY_STOCKS)
        results = []
        for stock in stocks:
            results.append({"id": stock[0], "name": stock[1]})
        return results

    def save(self, stock: StockCreate):
        db = DataBase()
        query = self.QUERY_CREATE_STOCK % f"'{stock.name}'"
        result = db.commit(query)
        return {"id": result[0], "name": stock.name}

    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_STOCKS_ID % id
        stock = db.execute(query, many=False)
        if stock:
            return {"id": stock[0], "name": stock[1]}
        return {}
