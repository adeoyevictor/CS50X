amount = 0

while True:
    print("Amount Due:", 50 - amount)
    x = int(input("Insert Coin: "))
    amount += x
    if amount >= 50:
        print("Change Owed:", amount - 50)
        break