from stats import num_words
from stats import num_of_char


def get_book_text(file_path: str):
    with open(file_path) as f:
        contens = f.read()
        return contens


def main():
    contens = num_words(get_book_text('./books/frankenstein.txt'))
    contens2 = num_of_char(get_book_text('./books/frankenstein.txt'))
    print(contens)
    print(contens2)


main()
