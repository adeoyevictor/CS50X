def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    nums = []
    if len(s) > 6 or len(s) < 2:
        return False
    if not s[:2].isalpha():
        return False
    for c in s:
        if c.isalpha() or c.isnumeric():
            pass
        else:
            return False
    for c in s:
        if c.isnumeric():
            nums += [int(c)]
    if len(nums) >= 1 and nums[0] == 0:
        return False
    print(s[-len(nums):])
    # if len(nums) >= 1:
        # if s[-len(nums):]





    print(nums)

    return True




main()