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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Добавлять можно объекты (товары) только класса продуктов.")

    @property
    def products(self) -> str:
        # Название продукта, 80 руб. Остаток: 15 шт.
        r = ""
        for product in self.__products:
            r += f"{product}\n"
        return r

    def __str__(self) -> str:
        count = 0
        for product in self.__products:
            count += product.quantity
        return f"{self.name}, количество продуктов: {count} шт."

    def average(self):
        count = 0
        for product in self.__products:
            count += product.quantity

        try:
            return count / len(self.__products)
        except ZeroDivisionError:
            return 0
