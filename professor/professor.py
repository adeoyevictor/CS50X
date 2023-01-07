import random


def main():
    level = get_level()
    generate_integer(level)



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
    while True:
        



if __name__ == "__main__":
    main()