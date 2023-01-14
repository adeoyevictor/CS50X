import pytest
from um import count


def test_word():
    assert count('um') == 1
    assert count('um?') == 1
    assert count(' UM ') == 1
    assert count('uM?') == 1

def test_sentence():
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2
