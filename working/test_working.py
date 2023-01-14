import pytest
from working import convert

def test_format1():
    with pytest.raises(ValueError):
        convert("9:00 to 13:00")

def test_format2():
    with pytest.raises(ValueError):
        convert("9 to 13")

def test_format2():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_valid_time():
    with pytest.raises(ValueError):
        convert("9:67 AM to 34:00 PM")

def test_result1():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'