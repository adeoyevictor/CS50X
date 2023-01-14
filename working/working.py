import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([0-9]{1,2}:?(?:[0-9]{2})? (?:AM|PM)) to ([0-9]{1,2}:?(?:[0-9]{2})? (?:AM|PM))$", s):
        start, stop = matches.groups()
        if check_valid_time(start) and check_valid_time(stop):
            print("Valid Time")
        else:
            raise ValueError("Invalid Time")

    else:
        raise ValueError("Invalid Time")

def check_valid_time(t):
    # am_or_pm = t[-2:]
    time = t.split(" ")[0]
    if ":" in time:
        hr, min = time.split(":")
        print(int(hr), int(min))
        if int(hr) > 12 or int(hr) < 1 or int(min) > 59 or int(min) < 0:
            return False
    else:
        print(int(time))
        if int(time) > 12 or int(time) < 1:
            return False
    return True


if __name__ == "__main__":
    main()