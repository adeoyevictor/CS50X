text = input("Input: ")

for c in text:
    if c.lower() in ["a", "e", "i", "o", "u"]:
        pass
    else:
        print(c, end="")
print()