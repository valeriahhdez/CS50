from bank import value
import pytest

def main():
    test_return_zero()
    test_return_20()
    test_return_100()

def test_return_zero():
    """ Test if value returns 0 when greeting is 'Hello' """
    assert value('hello') == 0

def test_return_20():
    """ Test if value returns 20 when greeting starts with 'H' """
    assert value('Hi') == 20

def test_return_100():
    """ Test if value returns 1000 when greeting is a sentence """
    assert value("What's up?") == 100
    assert value("Good Day") == 100

if __name__ == "__main__":
    main()
