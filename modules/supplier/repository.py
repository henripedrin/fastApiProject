from core.db import DataBase
from modules.supplier.schemas import SupplierCreate


class SupplierRepository(DataBase):
    QUERY_SUPPLIERS = "SELECT id,name FROM supplier"
    QUERY_SUPPLIER_ID = "SELECT id,name FROM company where supplier_id = %s"
    QUERY_CREATE_SUPPLIER = 'INSERT INTO supplier (name) VALUES (%s) RETURNING id;'

    def get_all(self):
        db = DataBase()
        suppliers = db.execute(self.QUERY_SUPPLIERS)
        results = []
        for supplier in suppliers:
            results.append({"id": supplier[0], "name": supplier[1]})
        return suppliers

    def save(self, supplier: SupplierCreate):
        db = DataBase()
        query = self.QUERY_CREATE_SUPPLIER % f"'{supplier.name}'"
        result = db.commit(query)
        return {"id": result[0], "name": supplier.name}

    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_SUPPLIER_ID % id
        supplier = db.execute(query, many=False)
        if supplier:
            return {"id": supplier[0], "name": supplier[1]}
        return{}
