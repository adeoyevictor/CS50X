import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([0-9]{1,2}:?(?:[0-9]{2})? (?:AM|PM)) to ([0-9]{1,2}:?(?:[0-9]{2})? (?:AM|PM))$", s):
        start, stop = matches.groups()
        if check_valid_time(start) and check_valid_time(stop):
            ...
        else:
            raise ValueError("Invalid Time")

    else:
        raise ValueError("Invalid Time")

def check_valid_time(t):
    print(t)
    am_or_pm = t[-1:]
    print(am_or_pm)
    return True


if __name__ == "__main__":
    main()