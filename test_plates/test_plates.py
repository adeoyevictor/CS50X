from plates import is_valid


def test_1():
    assert is_valid("CS50") == True
def test_2():
    assert is_valid("cs508") == True
def test_3():
    assert is_valid("HPACB") == True
def test_4():
    assert is_valid("EM") == True
