def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isalpha():
        return False
        
    if len(s) > 6 or len(s) < 2:
        return False
    for c in s:
        if c in [' ', '.', '!', '?']:
            return False
    nums = []
    for c in s:
        if c.isnumeric():
            nums += [int(c)]
    if len(nums) >= 1 and nums[0] == 0:
        return False
    return True




main()