# Shop - ядро для интернет-магазина

## Репозиторий

Проект доступен на GitHub: <https://github.com/mrMoish/Shop>

## Клонирование проекта

```bash
git clone https://github.com/mrMoish/Shop.git
```

Перейти в папку проекта:

```bash
cd Shop
```

## Зависимости

Проект использует [Poetry](https://python-poetry.org/) для управления зависимостями.

```bash
poetry install
```

Runtime-зависимостей на данный момент нет — проект пока представляет собой каркас (ядро) без внешних библиотек.

### Основные инструменты разработки

- `flake8` — линтер для проверки стиля кода
- `mypy` — статическая проверка типов
- `black` — автоформатирование кода
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
