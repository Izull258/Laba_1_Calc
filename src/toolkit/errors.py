"""Типы ошибок калькулятора и конвертера"""


class CalculatorError(ValueError):
    """Ошибка в арифметическом выражении"""


class ConversionError(ValueError):
    """Ошибка при переводе величины"""