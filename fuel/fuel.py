while True:
    try:
        text = input("Fraction: ")
        x = int(text[:1])
        y = int(text[2:])
        print(f"{int((x / y) * 100)}%")
        break
    except (ValueError,  ZeroDivisionError):
        pass

