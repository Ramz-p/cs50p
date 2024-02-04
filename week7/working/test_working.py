import pytest
from working import convert

def test_convert():
    # Test cases for valid input formats and expected output
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_value_error():
    # Test cases for invalid input formats raising ValueError
    with pytest.raises(ValueError):
        convert("9AM - 5PM")  # Missing space between hour and AM/PM
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")  # Incorrect format for AM/PM
    with pytest.raises(ValueError):
        convert("15:00 AM to 25:00 PM")  # Hour values out of valid range
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")  # Minute values out of valid range
