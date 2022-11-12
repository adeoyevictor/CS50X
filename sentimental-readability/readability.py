import from cs50 get_string

def main():
    text = get_string("Text: ")
    letters = count_letter(text)
    words = count_words(text)
    sentences = count_sentences(text)
    index = calc_index(letters, words, sentences)