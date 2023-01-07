import random


def main():
    get_level()



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
    pass



if __name__ == "__main__":
    main()