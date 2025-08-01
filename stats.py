# splits the text then counts the words
def num_of_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    print(f"{counter} words found in the document")    

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
    print(char_dict)