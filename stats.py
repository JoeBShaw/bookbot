# splits the text then counts the words
def num_of_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    print("-------- Word Count --------")
    print(f"Found {counter} total words")    
    

# counts the number of times each character is shown in the text
def character_counts(text):
    char_dict = {}
    counter = 1
    words = text.split()
    for word in words:
        for character in word.lower():
            if character not in char_dict:
                char_dict[character] = 1
            else:
                new_count = char_dict[character]
                new_count += 1
                char_dict[character] = new_count
    return char_dict

# the function for sorting the list of dictionaries by number
def sort_on(items):
    return items["num"]

# takes a dictionary and nests it inside a list
#sorts it and only saves letters from the characters 
def organised(dictionary):
    organised_list = []
    for character, count in dictionary.items():
        if character.isalpha() == True:
            organised_list.append({"char":character, "num": count})
        else:
            pass
    organised_list.sort(reverse=True, key=sort_on )
    print("-------- Characters Counted --------")
    return organised_list