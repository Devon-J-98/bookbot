def get_book_text(filepath):
    with open(filepath) as f:
    # do something with f (the file) here

        # f is a file object
        files = f.read()
    return files

def text_from_book():
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    number_of_words = len(words)
    return number_of_words
def main():
    # book_text = get_book_text("books/frankenstein.txt")
    value = text_from_book()
    print (value)


    




main()