class Product:
    name: str
    description: str
    __price: float
    quantity: int
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int, color:str=None) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    @classmethod
    def new_product(cls, param: dict) -> "Product":
        # return Product(param['name'], param['description'], param['price'], param['quantity'])
        return Product(**param)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int


    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str) -> None:
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory

    def __add__(self, other) -> float:
        if type(other) == self.__class__:
            return super().__add__(other)
        else:
            raise TypeError

class LawnGrass(Product):
    country: str # страна-производитель
    germination_period: int # срок прорастания
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str) -> None:
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period

    def __add__(self, other) -> float:
        if type(other) == self.__class__:
            return super().__add__(other)
        else:
            raise TypeError