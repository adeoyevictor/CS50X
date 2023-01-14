import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r'\b\W*um\W*\b', s, re.IGNORECASE)
    print(matches)
    return len(matches)


if __name__ == "__main__":
    main()