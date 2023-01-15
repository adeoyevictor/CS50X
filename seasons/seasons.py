from datetime import date
import re


def main():
    if check_format(input("Date of birth: ")):
        print("Valid")
    else:
        print("Invalid")


def check_format(d):
    return re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", d, re.IGNORECASE)

if __name__ == "__main__":
    main()