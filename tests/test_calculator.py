import pytest

from toolkit.calculator import evaluate, split_expression, validate_expression
from toolkit.errors import CalculatorError


def test_split_expression():
    assert split_expression("12.5 + 3 * 2") == ["12.5", "+", "3", "*", "2"]


def test_priority():
    assert evaluate("2 + 3 * 4") == 14.0


def test_division_and_addition():
    assert evaluate("10 / 4 + 2") == 4.5


def test_subtraction_order():
    assert evaluate("10 - 3 - 2") == 5.0


def test_division_order():
    assert evaluate("8 / 4 / 2") == 1.0


def test_negative_numbers():
    assert evaluate("-5 + 2 * -3") == -11.0


def test_unary_plus():
    assert evaluate("+5 + +2") == 7.0


def test_spaces():
    assert evaluate("  12\t+\n3  ") == 15.0


def test_decimal_numbers():
    assert evaluate("0.1 + 0.2") == pytest.approx(0.3)


def test_empty_expression():
    with pytest.raises(CalculatorError, match="Пустое выражение"):
        evaluate("   ")


def test_unknown_character():
    with pytest.raises(CalculatorError, match="Недопустимый символ"):
        evaluate("2 + a")


def test_missing_operand():
    with pytest.raises(CalculatorError, match="пропущено число"):
        evaluate("2 +")


def test_two_binary_operators():
    with pytest.raises(CalculatorError, match="Ожидалось число"):
        validate_expression(["2", "+", "*", "3"])


def test_missing_operator():
    with pytest.raises(CalculatorError, match="пропущена операция"):
        evaluate("2 3")


def test_division_by_zero():
    with pytest.raises(CalculatorError, match="Деление на ноль"):
        evaluate("10 / 0")


def test_two_decimal_points():
    with pytest.raises(CalculatorError, match="двух точек"):
        evaluate("1..2 + 3")


def test_dot_without_digits():
    with pytest.raises(CalculatorError, match="Точка без цифр"):
        evaluate("2 + .")
