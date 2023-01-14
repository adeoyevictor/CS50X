import pytest
from numb3rs import validate


def test_valid():
    assert validate("80.80.80.80") == True
    assert validate("10.10.10.10") == True
    assert validate("200.200.200.200") == True


def test_invalid():
    assert validate("800.80.80.80") == False
    assert validate("10.400.10.10") == False
    assert validate("200.256.200.200") == False