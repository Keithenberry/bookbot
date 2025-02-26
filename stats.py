def get_book_text(pathtofile):
    with open(pathtofile) as f:
        file_contents= f.read()
    return file_contents

def get_num_words(path):    
    text = get_book_text(path)
    words = text.split()
    num_words = 0

    for word in words:
        num_words += 1
    return num_words

def get_char_count(path):
    text = get_book_text(path)
    words_lower = text.lower()
    char_count = {}

    for char in words_lower:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

def get_count(char_dict): 
    return char_dict["count"]

def sort_chars(char_count_dict):
    chars_list = []
    for char, count in char_count_dict.items():
        chars_list.append({"char": char, "count": count})
    chars_list.sort(key=get_count, reverse=True) 
    return chars_list