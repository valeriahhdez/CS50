from numb3rs import validate
import pytest

def main():
    test_non_numeric_characters()
    test_greater_than_255()
    test_negative_values()
    test_all_zeros()
    test_valid_ipv4_address()

def test_non_numeric_characters():
    """Returns False for an IPv4 address with octets having non-numeric characters"""
    assert validate("192.168.a.1") == False
    assert validate("10.b.0.0") == False
    assert validate("172.16.c.1") == False
    assert validate("255.d.e.f") == False

def test_greater_than_255():
    """Returns False for an IPv4 address with octets having values greater than 255"""
    assert validate("256.0.0.0") == False
    assert validate("192.168.256.1") == False
    assert validate("10.0.0.256") == False
    assert validate("172.16.0.999") == False

def test_negative_values():
    """Returns False for an IPv4 address with octets having values less than 0"""
    assert validate("-1.0.0.0") == False
    assert validate("192.-168.0.1") == False
    assert validate("10.0.-0.0") == False
    assert validate("172.16.0.-1") == False

def test_all_zeros():
    """Validates an IPv4 address with all octets as 0"""
    assert validate("0.0.0.0") == True

def test_valid_ipv4_address():
    """Validates a valid IPv4 address with four octets separated by dots"""
    assert validate("192.168.0.1") == True
    assert validate("10.0.0.0") == True
    assert validate("172.16.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True