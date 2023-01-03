text = input("camelCase: ")

for c in text:
    if c.islower():
        print(c.lower(), end="")
    else:
        print(f"_{c.lower()}", end="")
print()