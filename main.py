def main():
    book_path = "books/frankenstein.txt"

    print(get_file_word_count(book_path))

def get_file_word_count(file):
    return get_word_count(read_file(file))

def read_file(file):
    with open(file) as f:
        return f.read()

def get_word_count(content):
    return len(content.split())

main()
