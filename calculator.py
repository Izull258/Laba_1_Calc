import argparse
import sys


def split_expression(expression):
    elements = []
    number = ""

    for char in expression:
        if char in "0123456789.":
            if char == "." and "." in number:
                raise ValueError("В числе не может быть двух точек")

            number = number + char
            continue

        if number != "":
            if number == ".":
                raise ValueError("Точка без цифр не является числом")

            elements.append(number)
            number = ""

        if char.isspace():
            continue

        if char in "+-*/":
            elements.append(char)
        else:
            raise ValueError("Недопустимый символ: " + char)

    if number != "":
        if number == ".":
            raise ValueError("Точка без цифр не является числом")

        elements.append(number)

    return elements


def validate_expression(elements):
    if not elements:
        raise ValueError("Пустое выражение")

    expect_number = True

    for element in elements:
        if expect_number:
            if element in ("+", "-"):
                continue

            if element in ("*", "/"):
                raise ValueError("Ожидалось число")

            expect_number = False

        else:
            if element not in ("+", "-", "*", "/"):
                raise ValueError("Между числами пропущена операция")

            expect_number = True

    if expect_number:
        raise ValueError("В конце выражения пропущено число")


parser = argparse.ArgumentParser(
    description="Разбор и проверка арифметического выражения"
)
parser.add_argument("expression", help="Выражение в кавычках")

args = parser.parse_args()

try:
    elements = split_expression(args.expression)
    validate_expression(elements)
    print(elements)
except ValueError as error:
    print("Ошибка:", error, file=sys.stderr)
    sys.exit(2)