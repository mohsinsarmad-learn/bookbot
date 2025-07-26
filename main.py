import sys


def get_book_text(filepath):
    print(f"Analyzing book found at {sys.argv[1]}...")
    with open(filepath) as file:
        return file.read()


from stats import get_number_of_words
from stats import get_number_of_characters_repeated, convert_to_sorted_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_content = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    number_of_words = get_number_of_words(book_content)
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    repeated_characters = get_number_of_characters_repeated(book_content)
    list_characters = convert_to_sorted_list(repeated_characters)
    for char_dict in list_characters:
        if char_dict["char"].isalpha():
            alphabet = char_dict["char"]
            count = char_dict["num"]
            print(f"{alphabet}: {count}")
    print("============= END ===============")


main()
