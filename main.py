from stats import get_num_words
from stats import get_num_character
from stats import into_keyvalue_pairs


def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]


    # book_path = "books/frankenstein.txt" # this is the path to the book
    text = get_book_text(book_path)
    num_words = get_num_words(text) # grabs the lenght from text from book
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    # print (f"{num_words} words found in the document")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # print(get_num_character(text))
    # into_keyvalue_pairs(get_num_character(text))
    sorted_char_list = into_keyvalue_pairs(get_num_character(text))
    for i in sorted_char_list:
        print(f'{i["char"]}: {i["num"]}')
    print("============= END ===============")




def get_book_text(filepath): # the should be called for the filepath in other functions
    with open(filepath) as f:
    # do something with f (the file) here

        # f is a file object
        files = f.read()
    return files

main()