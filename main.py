#importing functions from the other .py file
from stats import num_of_words, character_counts, organised

#getting the text from the book and reading it
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents 

#sorting the final list to make it more presentable
def dict_sorting(alist):
    for dictionary in alist:        
        char = dictionary.get("char")
        num = dictionary.get("num")
        print(f"{char}: {num}")

# main runs all the functions from both files
def main(input):
    print("======== BOOKBOT ========")
    print(f"Analysing book found at {input}")
    book_data = get_book_text(input)
    num_of_words(book_data)
    character_dict = character_counts(book_data)
    alist = organised(character_dict)
    dict_sorting(alist)
    print("======== END ========")

main("books/frankenstein.txt")