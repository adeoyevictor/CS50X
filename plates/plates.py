def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:2].isalpha() and s.isalnum() and len(s) >= 2 and len(s) <=6:
        for i in range(len(s)):
            if s[i].isnumeric():
                idx = i
                break
            


    return False


main()