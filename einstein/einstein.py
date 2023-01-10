try:
    mass = int(input("m: "))
    E = mass * (300000000 ** 2)
    print(f"E: {E}")
except ValueError:
    print("that's not an int")
    exit()
