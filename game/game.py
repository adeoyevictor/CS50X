import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level < 1:
            continue
        else:
            break

num = random
