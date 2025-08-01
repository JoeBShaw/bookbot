from stats import num_of_words, character_counts, organised

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents 

def main(input):
    book_data = get_book_text(input)
    num_of_words(book_data)
    character_dict = character_counts(book_data)
    organised(character_dict)

main("./books/frankenstein.txt")