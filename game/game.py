import random
import sys

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

num = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess < 1:
            continue
        else:
            if guess < num:
                print("Too small!")
                continue
            elif guess > num:
                print("Too large!")
                continue
            else:
                print("Just right!")
                sys.exit()