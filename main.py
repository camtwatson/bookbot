from stats import get_words
from stats import get_characters
from stats import sort_characters


def get_book_test(book):
    with open(book) as f:
        content = f.read()
#    print(content)
    get_words(content)
    get_characters(content)
    

def main():
    book = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_book_test(book)



main() 