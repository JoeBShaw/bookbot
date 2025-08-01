def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def num_of_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    print(f"{counter} words found in the document")    

def main(input):
    book_data = get_book_text(input)
    num_of_words(book_data)
    

main("./books/frankenstein.txt")