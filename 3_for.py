"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

from typing import TypedDict


class ProductSales(TypedDict):
    product: str
    items_sold: list[int]


def main() -> None:
    sales: list[ProductSales] = [
        {
            "product": "iPhone 12",
            "items_sold": [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186],
        },
        {
            "product": "Xiaomi Mi11",
            "items_sold": [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316],
        },
        {
            "product": "Samsung Galaxy 21",
            "items_sold": [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247],
        },
    ]
    for dictionary in sales:
        print(
            f"Суммарное количество продаж {dictionary['product']}: {sum(dictionary['items_sold'])}"
        )
    print()

    for dictionary in sales:
        print(
            f"Среднее количество продаж {dictionary['product']}:"
            f" {sum(dictionary['items_sold']) / len(dictionary['items_sold'])}"
        )
    print()

    print(
        f"Суммарное количество продаж: {
            sum(item for dictionary in sales for item in dictionary['items_sold'])
        }"
    )
    print()

    print(
        f"Среднее количество продаж всех типов: {
            sum(item for dictionary in sales for item in dictionary['items_sold'])
            / sum(len(dictionary['items_sold']) for dictionary in sales)
        }"
    )


if __name__ == "__main__":
    main()
