def main():
    text = input("Greeting: ").strip()
    res = value(text)
    print(res)



def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return f"$0"
    elif greeting.startswith("h"):
        return f"$20"
    else:
        return f"$100"


if __name__ == "__main__":
    main()










