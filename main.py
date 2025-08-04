def get_book_text(filepath):
    with open(filepath) as f:
    # do something with f (the file) here

        # f is a file object
        files = f.read()
    return files
    
def main():
    book_text = get_book_text("books/frankenstein.txt")
    print (book_text)


def number_of_words(text):
    text = book_text
    




main()