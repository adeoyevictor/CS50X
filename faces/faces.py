def convert(text):
    result = text.replace(":)", "🙂")
    result = text.replace(":(", "🙁")
    return result


def main():
    text = input("Enter a text: ")
    print(convert(text))

main()