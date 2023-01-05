lst = {}

while True:
    try:
        item = input("Item: ").upper()
        if item in lst:
            lst[item] += 1
        else:
            lst[item] = 0
    except EOFError:
        break
