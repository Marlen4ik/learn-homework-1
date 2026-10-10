"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def main() -> None:
    print("Кейс 0", accept_strings(1, "sd"))
    print("Кейс 1", accept_strings("as", "as"))
    print("Кейс 2", accept_strings("asas", "as"))
    print("Кейс 3", accept_strings("as", "learn"))


def accept_strings(str1: str, str2: str) -> int | None:
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0
    elif str1 == str2:
        return 1
    elif str1 != str2 and str1 > str2:
        return 2
    elif str1 != str2 and str2 == "learn":
        return 3

    return None


if __name__ == "__main__":
    main()
