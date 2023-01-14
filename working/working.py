import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([0-9]{1,2}:?(?:[0-9]{2})? (?:AM|PM)) to ([0-9]{1,2}:?(?:[0-9]{2})? (?:AM|PM))$", s):
        print(matches.group(1))
        print(matches.group(2))



if __name__ == "__main__":
    main()