while True:
    try:
        text = input("Fraction: ")
        x = int(text[:1])
        y = int(text[2:])
        percent =  int((x / y) * 100)
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{percent}%")
        break
    except (ValueError,  ZeroDivisionError):
        pass

