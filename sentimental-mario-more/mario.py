# TODO
from cs50 import get_int


def main():
    n = get_height()
    draw(n)

def get_height():
    while True:
        height = get_int("Height: ")
        if height in range(1, 9):
            break
    return height



def draw(height):
    # draw(height - 1)
    print(""*)


