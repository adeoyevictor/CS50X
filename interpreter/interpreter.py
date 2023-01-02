expression = input("Expression: ").strip()

x, y, z = expression.split(" ")

x = float(x)
z = float(z)

if y == "+":
    print(x + y)
elif y == "-":
    print(x - y)
elif y == "*":
    print(x * y)
elif y == "/":
    print(x / y)
