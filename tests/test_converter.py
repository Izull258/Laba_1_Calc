import pytest

from toolkit.converter import convert_units
from toolkit.errors import ConversionError


def test_centimeters_to_meters():
    result = convert_units(150, "cm", "m")
    assert result == 1.5
    assert isinstance(result, float)


def test_kilometers_to_millimeters():
    assert convert_units(1, "km", "mm") == 1000000.0


def test_grams_to_kilograms():
    assert convert_units(500, "g", "kg") == 0.5


def test_kilograms_to_grams():
    assert convert_units(2, "kg", "g") == 2000.0


def test_uppercase_units():
    assert convert_units(150, "CM", "M") == 1.5


def test_same_length_unit():
    assert convert_units(25, "m", "m") == 25.0


def test_celsius_to_kelvin():
    assert convert_units(0, "c", "k") == pytest.approx(273.15)


def test_kelvin_to_celsius():
    assert convert_units(273.15, "k", "c") == pytest.approx(0.0)


def test_fahrenheit_to_kelvin():
    assert convert_units(32, "f", "k") == pytest.approx(273.15)


def test_kelvin_to_fahrenheit():
    assert convert_units(273.15, "k", "f") == pytest.approx(32.0)


def test_celsius_to_fahrenheit():
    assert convert_units(0, "c", "f") == pytest.approx(32.0)


def test_fahrenheit_to_celsius():
    assert convert_units(32, "f", "c") == pytest.approx(0.0)


def test_celsius_to_celsius():
    assert convert_units(25, "c", "c") == 25.0


def test_fahrenheit_to_fahrenheit():
    assert convert_units(32, "f", "f") == 32.0


def test_kelvin_to_kelvin():
    assert convert_units(300, "k", "k") == 300.0


def test_absolute_zero_celsius():
    assert convert_units(-273.15, "c", "k") == pytest.approx(0.0)


def test_absolute_zero_fahrenheit():
    assert convert_units(-459.67, "f", "k") == pytest.approx(0.0)


def test_absolute_zero_kelvin():
    assert convert_units(0, "k", "k") == 0.0


def test_celsius_below_absolute_zero():
    with pytest.raises(ConversionError):
        convert_units(-300, "c", "k")


def test_fahrenheit_below_absolute_zero():
    with pytest.raises(ConversionError):
        convert_units(-500, "f", "c")


def test_negative_kelvin():
    with pytest.raises(ConversionError):
        convert_units(-1, "k", "f")


def test_invalid_celsius_to_same_unit():
    with pytest.raises(ConversionError):
        convert_units(-300, "c", "c")


def test_invalid_fahrenheit_to_same_unit():
    with pytest.raises(ConversionError):
        convert_units(-500, "f", "f")


def test_invalid_kelvin_to_same_unit():
    with pytest.raises(ConversionError):
        convert_units(-1, "k", "k")


def test_unknown_source_unit():
    with pytest.raises(ConversionError, match="исходная единица"):
        convert_units(1, "abc", "m")


def test_unknown_target_unit():
    with pytest.raises(ConversionError, match="конечная единица"):
        convert_units(1, "m", "abc")


def test_length_to_mass():
    with pytest.raises(ConversionError):
        convert_units(25, "m", "kg")


def test_temperature_to_mass():
    with pytest.raises(ConversionError):
        convert_units(25, "c", "kg")


def test_nan():
    with pytest.raises(ConversionError):
        convert_units(float("nan"), "cm", "m")


def test_infinity():
    with pytest.raises(ConversionError):
        convert_units(float("inf"), "cm", "m")


def test_negative_infinity():
    with pytest.raises(ConversionError):
        convert_units(float("-inf"), "cm", "m")
