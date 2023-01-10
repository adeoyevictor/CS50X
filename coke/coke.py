amount = 0

while True:
    print("Amount Due:", 50 - amount)
    try:
        x = int(input("Insert Coin: "))

    except:
        pass
    else:
        if x in [25, 10, 5]:
            amount += x
        else:
            continue
        if amount >= 50:
            print("Change Owed:", amount - 50)
            break