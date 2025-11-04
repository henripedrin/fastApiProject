from core.db import DataBase
from modules.Type.schemas import TypeCreate, Type


class ProductRepository:
    QUERY_TYPEPRODUCT = ("SELECT id, name FROM type_product")
    QUERY_TYPEPRODUCT_ID = "SELECT id, name FROM type_product where id = %s"
    QUERY_CREATE_TYPEPRODUCT = 'INSERT INTO type_product (name) VALUES ($s) RETURNING id'

    def get_all(self):
        db = DataBase()
        produtos = db.execute(self.QUERY_TYPEPRODUCT_ID)
        results = []
        for produto in produtos:
            results.append({"id" : produto[0], "name": produto[1]})
        return results

    def save(self, produto: Type):
        db = DataBase
        query = self.QUERY_CREATE_TYPEPRODUCT % f"'{produto.name}'"
        result = db.commit(query)
        return {"id": result[0], "name": produto.name}

    def get_id(self, id: int):
        db = DataBase
        query = self.QUERY_TYPEPRODUCT_ID % id
        produto = db.execute(query, many=False)
        if produto:
            return {"id": produto[0], "name": produto[1]}
        return {}