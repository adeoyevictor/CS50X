def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:2].isalpha():
        if len(s) >= 2 and len(s) <=6:
            for c in s:
                



    return False


main()