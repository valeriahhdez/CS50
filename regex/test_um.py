from um import count
import pytest

def main():
    test_single_um()
    test_um_as_part_of_word()
    test_um_at_boundary()
    test_um_surrounded_by_punctuation()
    test_um_surrounded_by_numbers()

    # Returns correct count when 'um' is used once in input string
def test_single_um():
    """Rrturns a positive integer when 'um' is a stand alone word"""
    assert count("This is um a test") == 1  

def test_um_as_part_of_word():
    """Returns 0 when um is part of a word, for example, 'umbrella'"""
    assert count("umbrella") == 0
    assert count("instrument") == 0

    
def test_um_at_boundary():
    """Returns an integer count when 'um' is at the beginning or end of input string"""
    assert count("um is at the beginning") == 1
    assert count("um is at the end um") == 2

def test_um_surrounded_by_punctuation():
    """Returns a positive integer when 'um' is a stand alone word regardless of surrounding 
    punctuation"""
    assert count("This is um, um!") == 2

def test_um_surrounded_by_numbers():
    assert count("123um456") == 0

def test_um_case_insensitive():
    """Tests case-insensitivity"""
    assert count("UM") == 1