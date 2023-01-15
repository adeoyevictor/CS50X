from datetime import date, timedelta
import re
import sys
import inflect

p = inflect.engine()


def main():
    dob = input("Date of birth: ")
    if check_format(dob):
        dob= date.fromisoformat(dob)
        today = date.today()
        days = (today - dob).days
        mins = days * 24 * 60

    else:
        sys.exit("Invalid Date")


def check_format(d):
    return re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", d, re.IGNORECASE)

if __name__ == "__main__":
    main()