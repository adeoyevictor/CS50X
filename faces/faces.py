def covert(text):
    result = text.replace(":)", "🙂")
    result = text.replace(":(", "🙁")
    return result


def main():
    text = input("Enter a text: ")
    print(convert(text))

if __name__ == "__main__"
    main()