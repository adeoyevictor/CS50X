import from cs50 get_string

def main():
    text = get_string("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    index = calc_index(letters, words, sentences)
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        printf(f"Grade {index}")


def count_letters():

def count_words(s):
    words = 1
    for i in s:
        if i == ' ':
            words += 1
    return words


def count_sentences():






















main()