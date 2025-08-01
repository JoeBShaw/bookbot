def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    print(file_contents)

def main(input):
    get_book_text(input)
    

main("./books/frankenstein.txt")