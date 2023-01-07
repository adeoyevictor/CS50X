def main():
    shorten()


def shorten(word):
    result = ''
    for c in word:
    if c.lower() in ["a", "e", "i", "o", "u"]:
        pass
    else:
        result += c
    return result


if __name__ == "__main__":
    main()






