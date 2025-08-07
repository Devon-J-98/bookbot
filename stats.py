def get_num_words(text):
    words = text.split() # splits the words into a list 
    return len(words) # grabs the lenght of the list aka how many words and returns it


def get_num_character(num_chars):
    letters = {}
    for letter in num_chars:
        if letter.lower() not in letters:
            letters[letter.lower()] = 0
        letters[letter.lower()] += 1
    return letters


def sort_on(items):
    return items["num"]

def into_keyvalue_pairs(list_of_letters):
    new_list = []
    for key, value in list_of_letters.items():
        if key.isalpha():
            new_list.append({"char": key, "num": value})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(items):
    return items["num"]