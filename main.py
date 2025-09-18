def get_book_text (file_path: str):
    with open(file_path) as f:
        contens = f.read()
        return contens


def main():
    contens = num_words(get_book_text('./books/frankenstein.txt'))
    print(contens)


def num_words(input : str):
    num_words_list = input.split()
    num_words = len(num_words_list)-1
    return f'{num_words} words found in the document'


main()
