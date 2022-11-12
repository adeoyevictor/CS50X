# TODO
from cs50 import get_int

height = None

while True:
    height = get_int("Height: ")
    if height in range(1, height+1):
        break