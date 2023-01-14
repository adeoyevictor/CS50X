import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches :=  re.search(r'^<iframe.+src="(https?)".*></iframe>$', s, re.IGNORECASE):




if __name__ == "__main__":
    main()