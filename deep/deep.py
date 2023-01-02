text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").replace("-", " ").lower()

if text == "42" or text == "forty two":
    print("Yes")
else:
    print("No")
