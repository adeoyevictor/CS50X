from datetime import date
import re
import sys


def main():
    if check_format(input("Date of birth: ")):
        today = date.today()
        print(today)
    else:
        sys.exit("Invalid Date")


def check_format(d):
    return re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", d, re.IGNORECASE)

if __name__ == "__main__":
    main()