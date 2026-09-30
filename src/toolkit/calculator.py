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


def calculate_multiply_divide(prepared):
    result = [prepared[0]]
    index = 1

    while index < len(prepared):
        operator = prepared[index]
        number = prepared[index + 1]

        if operator == "*":
            result[-1] = result[-1] * number

        elif operator == "/":
            if number == 0:
                raise ValueError("Деление на ноль")

            result[-1] = result[-1] / number

        else:
            result.append(operator)
            result.append(number)

        index = index + 2

    return result


def calculate_add_subtract(elements):
    result = elements[0]
    index = 1

    while index < len(elements):
        operator = elements[index]
        number = elements[index + 1]

        if operator == "+":
            result = result + number
        elif operator == "-":
            result = result - number

        index = index + 2

    return result


def prepare_numbers(elements):
    prepared = []
    expect_number = True
    sign = 1

    for element in elements:
        if expect_number:
            if element == "+":
                continue

            if element == "-":
                sign = -sign
                continue

            number = float(element) * sign
            prepared.append(number)

            sign = 1
            expect_number = False

        else:
            prepared.append(element)
            expect_number = True

    return prepared



def evaluate(expression):
    elements = split_expression(expression)
    validate_expression(elements)

    prepared = prepare_numbers(elements)
    after_multiply = calculate_multiply_divide(prepared)

    return calculate_add_subtract(after_multiply)