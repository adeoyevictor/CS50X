import pytest
from seasons import check_format

def test_dates():
    assert check_format("99-01-01") == False
    assert check_format("01-01-1999") == False
    assert check_format("01-1999-01") == False
    assert check_format("1999-01-01") == True
    assert check_format("2022-05-11") == True