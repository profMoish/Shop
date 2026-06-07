import pytest

from src.category import Category
from src.product import Product, Smartphone, LawnGrass


@pytest.fixture
def category1():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture
def category2():
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )


def test_category1(category1, category2):
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    # assert len(category1.__products) == 3

    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    # assert len(category2.products) == 1

    assert category1.product_count == 4
    assert category1.category_count == 2

    category2.add_product(Product("LG", "lorem", 150000.0, 8))
    assert category1.product_count == 5

    with pytest.raises(TypeError):
        category2.add_product(10)

    assert Category.product_count == 5

    category2.add_product(Smartphone('iPhone', 'lorem', 150000.0, 8, 15, '15', 512, 'Grey'))

    assert Category.product_count == 6

    category2.add_product(LawnGrass("iLawnGrass", 'lorem ipsum', 1000, 100,
                     'USA', 50, 'green'))

    assert Category.product_count == 7

def test_get_products(category2):
    assert '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n' == category2.products


def test_str_category(category1, category2, capsys):
    # Название категории, количество продуктов: 200 шт.
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."
    assert str(category2) == "Телевизоры, количество продуктов: 7 шт."
    print(category1)
    assert capsys.readouterr().out == "Смартфоны, количество продуктов: 27 шт.\n"
    print(category2)
    assert capsys.readouterr().out == "Телевизоры, количество продуктов: 7 шт.\n"
