import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches =  re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip, re.IGNORECASE)
    if matches:
        if int(matches.group(1)) 
    return False





if __name__ == "__main__":
    main()