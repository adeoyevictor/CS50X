from datetime import date
import re


def main():
    dob = check_format(input("Date of birth: "))


def check_format(d):
    return re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")

if __name__ == "__main__":
    main()