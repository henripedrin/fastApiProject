from modules.product.repository import ProductRepository
from modules.product.schemas import ProductCreate


class ProductService:
    def get_products(self):
        repository = ProductRepository()
        return repository.get_all()

    def create_product(self, product: ProductCreate):
        # VALIDAR OS CAMPOS DO CREATE AQUI
        if not product.name or product.name.strip() == "":
            raise ValueError("O nome é obrigatório")
        if len(product.name) > 255:
            raise ValueError("O nome é grande demais")

        repository = ProductRepository()
        existing = product.get_id()
        if existing:
            raise ValueError("Estoque já existe")

        return repository.save(product)

    def get_product_id(self, id: int):
        repository = ProductRepository()
        product = repository.get_id(id)
        return product


    def get_produtos_by_empresa(self, id):
        repository = ProductRepository()
        products = []
        products.append(repository.get_company_products())
        return products
