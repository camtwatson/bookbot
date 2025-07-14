def get_book_test(book):
    with open(book) as f:
        content = f.read()
#    print(content)
    get_words(content)


def get_words(content):
    words = content.split()
    maybe = len(words)
    print(f"{maybe} words found in the document.")

def main():
    book = "books/frankenstein.txt"
    get_book_test(book)


main()