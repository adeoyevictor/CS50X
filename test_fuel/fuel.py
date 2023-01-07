def main():
    ...


def convert(fraction):
    try:
        x, y = fraction.split("/")



def gauge(percentage):
    ...


if __name__ == "__main__":
    main()

while True:
    try:
        x , y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if x > y:
            continue
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
