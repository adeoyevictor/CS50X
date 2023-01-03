def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if not s[:2].isalpha():
        return False
    for c in s:
        if c.isalpha() or c.isnumeric():
            pass
        else:
            return False
    return True




main()