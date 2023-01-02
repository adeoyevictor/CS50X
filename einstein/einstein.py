try:
    mass = int(input("m: "))
except ValueError:
    print("that's not an int")
    exit()
else:
    E = mass * (300000000 ** 2)
    print(f"E: {E}")
