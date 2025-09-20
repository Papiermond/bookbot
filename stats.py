def num_words(input: str):
    num_words_list = input.split()
    num_words = len(num_words_list)
    return f'{num_words} words found in the document'


def num_of_char(input: str):
    cahrs = {}
    for c in input:
        lowered = c.lower()
        if lowered in cahrs:
            cahrs[lowered] += 1
        else:
            cahrs[lowered] = 1
    return cahrs
