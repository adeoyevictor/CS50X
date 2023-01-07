from plates import is_valid


def test_1():
    assert is_valid("CS50") == True
def test_2():
    assert is_valid("cs508") == True
def test_3():
    assert is_valid("HPACB") == True
    assert is_valid("HPA09") == False
def test_4():
    assert is_valid("EM") == True
    assert is_valid("89Mg") == False
    assert is_valid("89Mgtyhg") == False
