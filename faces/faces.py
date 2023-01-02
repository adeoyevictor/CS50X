def convert(text):
    result = text.replace(":)", "🙂").replace(":(", "🙁")
    return result


def main():
    text = input("Enter a text: ")
    print(convert(text))

main()