from stats import get_words
def get_book_test(book):
    with open(book) as f:
        content = f.read()
#    print(content)
    get_words(content)

def main():
    book = "books/frankenstein.txt"
    get_book_test(book)


main()