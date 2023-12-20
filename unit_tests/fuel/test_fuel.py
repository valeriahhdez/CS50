import pytest
from unit_tests.fuel.re_fuel import convert, gauge


def test_convert_valid_fraction():
    """Tests conversion of a valid fraction to a percentage."""
    assert convert("5/10") == 50

def test_convert_fraction_with_decimals():
    """Tests handling of fractions with decimals."""
    with pytest.raises(ValueError):
        convert("5.5/10")

def test_convert_fraction_with_non_integers():
    """Tests handling of fractions with non-integer values."""
    with pytest.raises(ValueError):
        convert("5/hello")

def test_convert_fraction_with_x_greater_than_y():
    """Tests handling of fractions where X > Y."""
    with pytest.raises(ValueError):
        convert("10/5")

def test_convert_fraction_with_zero_denominator():
    """Tests handling of fractions with a zero denominator."""
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_convert_invalid_format():
    """Tests handling of invalid fraction formats."""
    with pytest.raises(ValueError):
        convert("5-10")

def test_convert_missing_numbers():
    """Tests handling of fractions missing numbers."""
    with pytest.raises(ValueError):
        convert("5/")

def test_gauge_full():
    """Tests checking if 'F' is returned when percentage >= 99"""
    assert gauge(99) == 'F'

def test_gauge_empty():
    """Tests checking if 'E' is returned when percentage <= 1"""
    assert gauge(1) == 'E'

def test_gauge_percentage():
    """Tests checking if gauge is returnes f{percentage}% when 1 < percentage > 99"""
    assert gauge(88) == f'{88}%'
    assert gauge (12) == f'{12}%'
   
