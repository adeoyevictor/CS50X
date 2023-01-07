from plates import is_valid

def test_2():
    assert is_valid("cs") == True
    assert is_valid("45") == False

def test_1():
    assert is_valid("CS50WERGH") == False
    assert is_valid("C") == False
    assert is_valid("CS50") == True

def test_3():
    assert is_valid("cs50") == True
    assert is_valid("cs50%@") == False
def test_4():
    assert is_valid("cs50") == True
    assert is_valid("cs05") == False
    assert is_valid("cs50p") == False

