from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert("4.5")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("6/3")
    with pytest.raises(ZeroDivisionError):
        convert("6/0")
    assert convert("3/4") == 75

def test_gauge():
    pass
