import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search(r"^[0-9]{1,2}:?([0-9]{2})? (AM|PM) to [0-9]{1,2}:?([0-9]{2})? (AM|PM)$", s):
        print("Yes")


if __name__ == "__main__":
    main()