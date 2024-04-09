def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    words_in_text = count_words_in_book(text)
    print(f"There are {words_in_text} words in the text.")

def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception as e:
        print(e)

def count_words_in_book(book):
    words = book.split()
    return len(words)

main()