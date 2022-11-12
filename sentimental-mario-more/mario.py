# TODO
from cs50 import get_int

# height = None
def get_height():
    while True:
        height = get_int("Height: ")
        if height in range(1, 9):
            break
    return height

n = get_height()

