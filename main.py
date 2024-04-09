def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_in_text = count_words_in_book(text)
    chars_dict = char_occurence_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f" --- Begin report of {book_path} ---")
    print(f"There are {words_in_text} words in the text.")
    print("\n\n")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report. ---")


def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception as e:
        print(e)

def count_words_in_book(book):
    words = book.split()
    return len(words)

def char_occurence_dict(book):
    chars_dict = {}
    for c in book:
        lower = c.lower()
        if lower in chars_dict:
            chars_dict[lower] += 1
        else:
            chars_dict[lower] = 1
    return chars_dict

def sort_dict(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_dict)
    return sorted_list

main()