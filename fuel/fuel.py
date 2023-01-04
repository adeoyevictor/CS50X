while True:
    try:
        x , y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        percent =  round((x / y) * 100)
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{percent}%")
        break
    except (ValueError,  ZeroDivisionError):
        pass

