import math

from toolkit.errors import ConversionError


def celsius_to_kelvin(value: float) -> float:
    """Проверяет абсолютный ноль и переводит градусы Цельсия в кельвины"""
    if value < -273.15:
        raise ConversionError("Температура ниже абсолютного нуля")

    return value + 273.15

def kelvin_to_celsius(value: float) -> float:
    """Проверяет абсолютный ноль и переводит кельвины в градусы Цельсия"""
    if value < 0:
        raise ConversionError("Температура ниже абсолютного нуля")

    return value - 273.15

def fahrenheit_to_kelvin(value: float) -> float:
    """Проверяет абсолютный ноль и переводит градусы Фаренгейта в кельвины"""
    if value < -459.67:
        raise ConversionError("Температура ниже абсолютного нуля")

    return (value + 459.67) * 5 / 9

def kelvin_to_fahrenheit(value: float) -> float:
    """Проверяет абсолютный ноль и переводит кельвины в градусы Фаренгейта"""
    if value < 0:
        raise ConversionError("Температура ниже абсолютного нуля")

    return value * 9 / 5 - 459.67


def convert_units(value: float, from_unit: str, to_unit: str) -> float:
    """Проверяет число и единицы, затем переводит длину, массу или температуру"""
    if not math.isfinite(value):
        raise ConversionError("Введите конечное число")
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    groups = {
        "mm": "length",
        "cm": "length",
        "m": "length",
        "km": "length",
        "g": "mass",
        "kg": "mass",
        "c": "temperature",
        "f": "temperature",
        "k": "temperature",
    }

    if from_unit not in groups:
        raise ConversionError("Неизвестная исходная единица")

    if to_unit not in groups:
        raise ConversionError("Неизвестная конечная единица")

    if groups[from_unit] != groups[to_unit]:
        raise ConversionError("Нельзя переводить между разными группами величин")

    if from_unit == "c" and to_unit == "k":
        return celsius_to_kelvin(value)

    if from_unit == "k" and to_unit == "c":
        return kelvin_to_celsius(value)

    if from_unit == "f" and to_unit == "k":
        return fahrenheit_to_kelvin(value)

    if from_unit == "k" and to_unit == "f":
        return kelvin_to_fahrenheit(value)

    if from_unit == "c" and to_unit == "f":
        kelvin = celsius_to_kelvin(value)
        return kelvin_to_fahrenheit(kelvin)

    if from_unit == "f" and to_unit == "c":
        kelvin = fahrenheit_to_kelvin(value)
        return kelvin_to_celsius(kelvin)

    if from_unit == "c" and to_unit == "c":
        celsius_to_kelvin(value)
        return float(value)

    if from_unit == "f" and to_unit == "f":
        fahrenheit_to_kelvin(value)
        return float(value)

    if from_unit == "k" and to_unit == "k":
        if value < 0:
            raise ConversionError("Температура ниже абсолютного нуля")
        return float(value)
            
    factors = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "g": 0.001,
        "kg": 1,
    }
    
    base_value = value * factors[from_unit]
    result = base_value / factors[to_unit]

    return result
