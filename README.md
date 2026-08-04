# Shop — ядро для интернет-магазина

Проект на Python: базовые доменные классы `Product` (товар) и `Category` (категория товаров) для интернет-магазина, покрытые тестами.

## Возможности

- **`Product`** — товар с названием, описанием, количеством и ценой
  - Цена хранится в приватном поле и доступна через свойство `price`
  - Сеттер `price` не позволяет установить нулевую или отрицательную цену — вместо этого выводит предупреждение и оставляет прежнее значение
  - Альтернативный конструктор `Product.new_product(dict)` — создание товара из словаря параметров
- **`Category`** — категория с названием, описанием и списком товаров
  - `add_product()` — добавление товара в категорию
  - `products` — текстовое представление всех товаров категории (`Название, цена руб. Остаток: N шт.`)
  - Классовые счётчики `Category.category_count` и `Category.product_count` — общее число созданных категорий и товаров во всех категориях

## Структура проекта

```
Shop/
├── src/
│   ├── product.py     # класс Product
│   └── category.py    # класс Category
├── tests/
│   ├── test_product.py
│   └── test_category.py
├── pyproject.toml     # зависимости и конфигурация (Poetry)
└── .flake8            # конфигурация линтера
```

## Требования

- Python 3.14+
- [Poetry](https://python-poetry.org/) для управления зависимостями

## Установка

```bash
git clone https://github.com/mrMoish/Shop.git
cd Shop
poetry install
```

## Тесты и линтинг

```bash
poetry run pytest --cov=src
poetry run flake8
poetry run mypy src
poetry run black .
poetry run isort .
```

Настройки инструментов заданы в `pyproject.toml` и `.flake8`:

- `black` — длина строки 119 символов
- `isort` — длина строки 119 символов
- `mypy` — строгий режим (`disallow_untyped_defs`, `no_implicit_optional`, `warn_return_any`)

## Зависимости

Проект не имеет внешних runtime-зависимостей — только dev-инструменты:

| Группа | Пакет | Назначение |
|---|---|---|
| lint | `flake8` | проверка стиля кода |
| lint | `mypy` | статическая проверка типов |
| lint | `black` | автоформатирование |
| lint | `isort` | сортировка импортов |
| dev | `pytest-cov` | тестирование и измерение покрытия |

## Лицензия

Не указана.- `black` — автоформатирование кода
- `isort` — сортировка импортов

### Инструменты тестирования

- `pytest-cov` — измерение покрытия тестами

## Запуск проверок

```bash
poetry run flake8
poetry run mypy .
poetry run black --check .
poetry run isort --check-only .
```

## Запуск тестов

```bash
poetry run pytest --cov
```

HTML-отчёт о покрытии тестами формируется в папке `htmlcov/`.
