import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search(r"^[0-9]{1,2}$", s):
        print("Yes")


if __name__ == "__main__":
    main()