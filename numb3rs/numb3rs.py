import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches =  re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip, re.IGNORECASE)
    if matches:
        list_of_matches = []
        for i in range(4):
            list_of_matches.append(int(matches.group(i+1)))
        print(list_of_matches)
        for num in list_of_matches:
            if num < 0 or num > 255:
                return False
            else:
                return True
        return True
    return False





if __name__ == "__main__":
    main()