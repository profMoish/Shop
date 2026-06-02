from src.product import Product


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        # Название продукта, 80 руб. Остаток: 15 шт.
        r = ""
        for product in self.__products:
            r += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return r
