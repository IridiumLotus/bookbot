def main():
    book_path = "/home/iridium/workspace/github.com/iridiumLotus/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(f"--- Report of {book_path} ---")
    word_count = count_words(text)
    print(f"{word_count} words in the document")
    print()
    for item in count_characters(text):
        print(f"The '{item['char']}' character was found {item['count']} times")

def count_characters(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
          if char not in characters:
                characters[char] = 1
          else:
              characters[char] += 1
    
    return sort_character_dict(characters)

def sort_character_dict(count_characters_dict):
    char_dicts = [{"char": key, "count": value} for key, value in count_characters_dict.items()]
    sorted_char_dicts = sorted(char_dicts, key=lambda d: d["count"], reverse=True)
    return sorted_char_dicts

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

main()