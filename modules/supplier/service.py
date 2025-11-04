from modules.supplier.repository import SupplierRepository
from modules.supplier.schemas import SupplierCreate

class SupplierService:
    def get_suppliers(self):
        repository = SupplierRepository()
        return repository.get_all()

    def create_supplier(self, supplier: SupplierCreate):

        if not supplier.name or supplier.name.strip() == "":
            raise ValueError("O nome é obrigatório")
        if len(supplier.name) > 255:
            raise ValueError("O nome grande demais")

        repository = SupplierRepository()
        existing = supplier.get_id()
        if existing:
            raise ValueError("Fornecedor já existe")

        return repository.save(supplier)

    def get_supplier_id(self, id: int):
        repository = SupplierRepository()
        supplier = repository.get_id(id)
        return supplier
