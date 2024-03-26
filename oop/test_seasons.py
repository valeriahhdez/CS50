import pytest
from seasons import convert_to_minutes, convert_to_words

def test_convert_to_minutes():
    # Test with a valid date
    assert convert_to_minutes('2000-01-01') == 'Twelve million, seven hundred forty-four thousand minutes'
    # Test with an invalid date
    with pytest.raises(SystemExit) as e:
        convert_to_minutes('1999/01/01')
    assert e.type == SystemExit
    assert e.value.code == 1

def test_convert_to_words():
    # Test with a positive integer
    assert convert_to_words(1000) == 'One thousand minutes'
    # Test with a non-integer input
    with pytest.raises(Exception):
        convert_to_words('abc')