from stats import count_words, count_characters, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

def main():
    booktext = get_book_text("./books/frankenstein.txt")
    
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

    

main()