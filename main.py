from stats import count_words, count_characters, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

def main():
    #booktext = get_book_text("./books/frankenstein.txt")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    booktext = get_book_text(path_to_book)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    number_of_words = count_words(booktext)
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    number_of_chars = count_characters(booktext)
    dict_list = sort_dict(number_of_chars)
       
    for dict in dict_list:
        if dict["char"].isalpha():
            char = dict["char"]
            number = dict["num"] 
            print(f"{char}: {number}")
    
    print("============= END ===============")

    

main()