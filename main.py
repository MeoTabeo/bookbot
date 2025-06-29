from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

def main():
    booktext = get_book_text("./books/frankenstein.txt")
    # print(booktext)
    number_of_words = count_words(booktext)
    print(f"{number_of_words} words found in the document")

main()