from core.db import DataBase
from modules.product.schemas import ProductCreate


class ProductRepository:
    QUERY_PRODUCT = "SELECT id, name FROM product;"
    QUERY_PRODUCT_ID = "SELECT id, name FROM product WHERE id = %s;"
    QUERY_CREATE_PRODUCT = "INSERT INTO product (name) VALUES (%s) RETURNING id;"
    QUERY_COMPANY = """
        SELECT
            p.name AS produto,
            tp.name AS tipo_produto,
            s.name AS fornecedor,
            c.name AS empresa
        FROM product p
        INNER JOIN company c ON c.id = p.company_id
        INNER JOIN supplier s ON s.id = p.supplier_id
        INNER JOIN type_product tp ON tp.id = p.type_product_id
        WHERE c.id = %s;
    """

    def get_all(self):
        db = DataBase()
        products = db.execute(self.QUERY_PRODUCT)
        results = []
        for product in products:
            results.append({"id": product[0], "name": product[1]})
        return results

    def save(self, product: ProductCreate):
        db = DataBase()
        query = self.QUERY_CREATE_PRODUCT % f"'{product.name}'"
        result = db.commit(query)
        return {"id": result[0], "name": product.name}

    def get_id(self, id: int):
        db = DataBase()
        product = db.execute(self.QUERY_PRODUCT_ID, (id,))
        if product:
            return {"id": product[0], "name": product[1]}
        return {}

    def get_company_products(self, id: int):
        db = DataBase()
        products = db.execute(self.QUERY_COMPANY, (id,))
        results = []
        for row in products:
            results.append({
                "produto": row[0],
                "tipo_produto": row[1],
                "fornecedor": row[2],
                "empresa": row[3]
            })
        return results
