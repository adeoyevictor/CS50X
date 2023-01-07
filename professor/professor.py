import random
# import sys

def main():
    level = get_level()
    score = 0
    for i in range(10):
        try:
            x = generate_integer(level)
            y = generate_integer(level)
        except ValueError:
            pass
        else:
            for i in range(3):
                try:
                    ans = int(input(f"{x} + {y} = "))
                except ValueError:
                    print("EEE")
                else:
                    if ans == x + y:
                        score += 1
                        break
                    else:
                        if i == 2:
                            print(f"{x} + {y} = {x + y}")
                            continue
                        else:
                            print("EEE")
                            continue
    print("Score: {score}")







def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                continue
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        rand_int = random.randint(0, 9)
    elif level == 2:
        rand_int = random.randint(10, 99)
    elif level == 3:
        rand_int = random.randint(100, 999)
    else:
        raise ValueError
    return rand_int





if __name__ == "__main__":
    main()