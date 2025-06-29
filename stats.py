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
