
from stats import get_num_words, get_num_char
def main():
    with open("books/frankenstein.txt") as f:
        book_text = f.read()
    word_count = get_num_words(book_text)
    print(f"{word_count} words found in the document")
    char_count = get_num_char(book_text)
    print(char_count)
main()


