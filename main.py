import sys
from stats import get_num_words, get_num_char, convert_dict_to_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    with open(book_path) as f:
        book_text = f.read()
    
    word_count = get_num_words(book_text)
    print("\n----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    char_count = get_num_char(book_text)
    sorted_chars = convert_dict_to_sorted_list(char_count)
    print("\n--------- Character Count -------")
    for char_info in sorted_chars:
        if char_info['char'].isalpha():  # only print if character is a letter
            print(f"{char_info['char']}: {char_info['count']}")

main()


