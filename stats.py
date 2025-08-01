# splits the text then counts the words
def num_of_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    print(f"{counter} words found in the document")    
