import pytest

from src.product import Product


@pytest.fixture
def product1() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

@pytest.fixture
def product2() -> Product:
    return Product.new_product({"name": "Iphone 14", "description": "512GB, Gray space", "price": 150000.0, "quantity": 5})

def test_product1(product1, capsys) -> None:
    assert product1.name == "Iphone 15"
    assert product1.description == "512GB, Gray space"
    assert product1.price == 210000.0
    assert product1.quantity == 8
    product1.price = 220000.0
    assert product1.price == 220000.0
    product1.price = -1
    captured = capsys.readouterr()
    assert captured.out == 'Цена не должна быть нулевая или отрицательная\n'


def test_product2(product2) -> None:
    assert product2.name == "Iphone 14"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 150000.0
    assert product2.quantity == 5

# @pytest.mark.parametrize('product1, product2', [])