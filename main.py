from stats import get_words
from stats import get_characters
from stats import sort_characters
import sys

def check_args():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(sys.argv[1])
    return sys.argv[1]

def get_book_test(book):
    with open(book) as f:
        content = f.read()
#    print(content)
    get_words(content)
    get_characters(content)


def main():
    check_args()
    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_book_test(book)



main() 