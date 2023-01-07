from bank import value

def test_1():
    assert value("hello") == "$0"
    assert value("Hello") == "$0"

def test_2():
    assert value("hi") == "$20"
    assert value("Hey") == "$20"

def test_2():
    assert value("good morning") == "$100"
    assert value("good evening") == "$100"