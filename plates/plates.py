def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[:2].isalpha():
        return False
    if len(s) > 6 or len(s) < 2:
        return False
    for c in s:
        if not c.isalpha() or c.isnumeric():
            return False
    return True




main()