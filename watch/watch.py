import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches :=  re.search(r'^<iframe.+src="(https?://(www)?\.youtube.com/embed/xvFZjo5PgG0)".*></iframe>$', s, re.IGNORECASE):




if __name__ == "__main__":
    main()