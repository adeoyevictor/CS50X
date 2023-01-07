from twttr import shorten

def test_hello():
    assert shorten("Hello") == "Hll"

def test_World():
    assert shorten("World") == "Wrld"