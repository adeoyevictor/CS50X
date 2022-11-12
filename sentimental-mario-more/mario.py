# TODO
from cs50 import get_int
def draw(n):
    if n < 1:
        return
    draw(n - 1)
    print(' ' * (n), end='')
    print('#' * n, end='')
    print(' ' * 2, end='')
    print('#' * n)

while True:
    height = get_int("Height: ")
    if height in range(1, 9):
        break

draw(height)









