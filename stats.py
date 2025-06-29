def count_words(text):
    word_list = text.split()
    count = len(word_list)
    return count

def count_characters(text):
    lowertext = text.lower()
    dict = {}
    for char in lowertext:
         if char in dict:
            counter = dict[char]
         else:
            counter = 0

         counter += 1
         dict[char] = counter
    return dict

def sort_dict(dict):
    list_of_dicts = []
    for char in dict:
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = dict[char]
        list_of_dicts.append(new_dict)
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def sort_on(items):
    return items["num"]