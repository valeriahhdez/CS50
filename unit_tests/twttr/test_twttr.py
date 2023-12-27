from re_twttr import shorten
import pytest

def test_only_vowels():
    assert shorten("aeiou") == ""

def test_no_vowels():
    assert shorten("bcdfg") == "bcdfg"

def test_empty_string():
    assert shorten("") == ""

def test_numbers():
    assert shorten('12345') == "12345"

def test_punctuation():
    assert shorten("bhg!") == "bhg!"