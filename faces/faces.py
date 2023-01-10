def main():
    text = input("Enter a text: ")
    print(convert(text))


def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


main()