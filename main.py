import sys
from stats import get_num_words, get_char_count, sort_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path to book>")
    sys.exit(1)

path = sys.argv[1]
word_count = get_num_words(path)
char_count = get_char_count(path)
sorted_characters = sort_chars(char_count)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]} ...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")

for char_dict in sorted_characters:
    if char_dict["char"].isalpha():
        print(f'{char_dict["char"]}: {char_dict["count"]}')

print("============= END ===============")