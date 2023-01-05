lst = {}

while True:
    try:
        item = input("Item: ").upper()
        if item in lst:
            lst[item] += 1
        else:
            lst[item] = 1
    except EOFError:
        print()
        break

for item in lst:
    print(item)
