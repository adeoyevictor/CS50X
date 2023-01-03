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
        if not c.isalpha() or c.isnumeric():
            return False
    nums = []
    for c in s:
        if c.isnumeric():
            nums += [int(c)]
    if len(nums) >= 1 and nums[0] == 0:
        return False
    if len(nums) >= 1:
        if not s[-len(nums):].isnumeric():
            return False
    return True




main()