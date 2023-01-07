import random
# import sys

def main():
    level = get_level()
    # try:
    #     rand_int = generate_integer(level)
    #     print(rand_int)
    # except ValueError:
    #     print("Val Error")
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
                    if ans == x + y:
                        break
                    else:
                        print("EEE")
                        continue
                except ValueError:
                    print("EEE")







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