# TODO
from cs50 import get_int

n = 0

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
    if height < 1:
        return
    draw(height - 1)

    print(' ' * (height), end='')
    print('#' * height, end='')
    print(' ' * 2, end='')
    print('#' * height)


main()