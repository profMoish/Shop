import pytest

from src.product import Product
from src.product import Smartphone
from src.product import LawnGrass

@pytest.fixture
def product1() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product2() -> Product:
    return Product.new_product(
        {"name": "Iphone 14", "description": "512GB, Gray space", "price": 150000.0, "quantity": 5}
    )

@pytest.fixture
def smartphone() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8,
                      5, '15', 512, 'Gray space')


@pytest.fixture
def lawngrass() -> LawnGrass:
    return LawnGrass("iLawnGrass", 'lorem ipsum', 1000, 100,
                     'USA', 50, 'green')

def test_product1(product1, capsys) -> None:
    assert product1.name == "Iphone 15"
    assert product1.description == "512GB, Gray space"
    assert product1.price == 210000.0
    assert product1.quantity == 8
    product1.price = 220000.0
    assert product1.price == 220000.0
    product1.price = -1
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_product2(product2) -> None:
    assert product2.name == "Iphone 14"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 150000.0
    assert product2.quantity == 5


def test_str_product(product1, product2, capsys) -> None:
    assert str(product1) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    print(product1)
    assert capsys.readouterr().out == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"

    assert str(product2) == "Iphone 14, 150000.0 руб. Остаток: 5 шт."
    print(product2)
    assert capsys.readouterr().out == "Iphone 14, 150000.0 руб. Остаток: 5 шт.\n"


def test_add_product(product1, product2) -> None:
    assert product1 + product2 == 210000 * 8 + 150000 * 5

def test_smartphone(smartphone) -> None:
    assert smartphone.name == "Iphone 15"
    assert smartphone.description == "512GB, Gray space"
    assert smartphone.price == 210000.0
    assert smartphone.quantity == 8
    assert smartphone.efficiency == 5
    assert smartphone.model == '15'
    assert smartphone.memory == 512
    assert smartphone.color == 'Gray space'

def test_lawngrass(lawngrass) -> None:
    assert lawngrass.name == "iLawnGrass"
    assert lawngrass.description == "lorem ipsum"
    assert lawngrass.price == 1000
    assert lawngrass.quantity == 100
    assert lawngrass.country == 'USA'
    assert lawngrass.germination_period == 50
    assert lawngrass.color == 'green'

def test_smartphone_add_lawngrass(smartphone, lawngrass) -> None:
    with pytest.raises(TypeError):
        smartphone + lawngrass
    with pytest.raises(TypeError):
        lawngrass + smartphone
    assert smartphone + smartphone == 3360000
    assert lawngrass + lawngrass == 200000