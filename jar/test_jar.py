import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar1 = Jar(5)
    assert jar1.capacity == 5
    assert jar1.size == 0
    ...


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(7)
    ...



def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(7)
    jar.withdraw(5)
    assert jar.size ==0
    ...
