import validators

def main():
    print(val(input("Whats your email? ")))

def val(s):
    return "Valid" if validators.email(s) == True else "Invalid"


if __name__ == "__main__":
    main()