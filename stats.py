def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    char_count = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["count"]

def convert_dict_to_sorted_list(char_count_dict):
    char_list = []
    for char, count in char_count_dict.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list