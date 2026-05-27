import pytest

from src.product import Product


@pytest.fixture
def product1() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_product1(product1) -> None:
    assert product1.name == "Iphone 15"
    assert product1.description == "512GB, Gray space"
    assert product1.price == 210000.0
    assert product1.quantity == 8
