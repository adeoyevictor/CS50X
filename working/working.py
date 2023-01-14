import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    re.search(r"^[0-]$", s)


if __name__ == "__main__":
    main()