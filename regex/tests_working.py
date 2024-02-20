from working import convert
import pytest

def main():
    test_valid_time_range
    test_valid_time_range
    test_invalid_time
    test_invalid_minutes

def test_valid_time_range():
    """Tests for valid time range """
    assert convert("10:30 AM to 2:45 PM") == "10:30 to 14:45"

def test_valid_time():
        """Tests for valid time format"""
        assert convert("10 PM to 6:30 AM") == "22:00 to 06:30"

    # Raises ValueError if start hour > 12 and period is 'PM'
def test_invalid_time():
    """Tests for invalid time format"""
    with pytest.raises(ValueError):
        convert("13:00 PM to 2:00 PM")
        convert("2 PM to 17:00 PM")
        convert ("2 PM - 7 PM")
        convert ("2 PM 7 PM")


def test_invalid_minutes():
        """Tests for invalid minutes"""
        with pytest.raises(ValueError):
            convert("9:60 AM to 10:30 AM")
            convert("9:60 AM to 10:61 PM")