from modules.Type.repository import ProductRepository
from modules.Type.schemas import TypeCreate


class ProductService:
    def get_products(self):
        repository = ProductRepository
        return repository.get_all()

    def create_product(self, product: TypeCreate):
        if not product.name or product.name.strip() == "":
            raise ValueError("O nome é obrigatório")
        if len(product.name) > 255:
            raise ValueError("O nome é grande demais")

        repository = ProductRepository()
        existing = product.get_id()
        if existing:
            raise ValueError("Tipo de produto já existe")

        return repository.save(product)

    def get_product_id(self, id: int):
        repository = ProductRepository()
        product = repository.get_id(id)
        return product
