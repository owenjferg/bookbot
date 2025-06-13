from stats import *
file = "books/frankenstein.txt"
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

text = get_book_text(file)

word_count = get_book_words(file)
chars = get_book_characters(text)
char_list = create_char_list(chars)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {file}")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for line in char_list:
    print(line)
print("============= END ===============")
