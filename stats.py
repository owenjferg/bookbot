def get_book_words(filepath):
    with open(filepath) as f:
        text = f.read()
        words = text.split()
        return len(words)

def get_book_characters(book_text):
    char_counts = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        else:
            char_counts[lower_char] = 1
    return char_counts

def create_char_list(char_counts):
    # Filter to only alphabetic characters
    filtered = {char: count for char, count in char_counts.items() if char.isalpha()}
    
    # Sort characters by frequency (descending)
    sorted_items = sorted(filtered.items(), key=lambda x: x[1], reverse=True)
    
    # Build the list
    char_list = []
    for char, count in sorted_items:
        char_list.append(f"{char}: {count}")
    
    return char_list

