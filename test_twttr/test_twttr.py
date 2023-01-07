from twttr import shorten

def test_hello():
    assert shorten("Hello") == "Hll"
    assert shorten("hello") == "hll"
    assert shorten("hello1") == "hll1"

def test_World():
    assert shorten("World") == "Wrld"
    assert shorten("World,") == "Wrld,"
    assert shorten("WOrld,") == "Wrld,"