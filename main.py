def main():
    book_path = "books/frankenstein.txt"
    book_content = read_file(book_path)
    word_count = get_word_count(book_content)
    letters_count = sort_dictionary(get_letter_count(book_content))

    print(f"--Begining Report of {book_path}\n")
    print(f"There are {word_count} words in the document...\n")
    
    for i in letters_count.keys():
        print(f"\'{i}\' was found {letters_count[i]} times..")

    print("\n-- End of Report --")

def get_file_word_count(file):
    return get_word_count(read_file(file))

def read_file(file):
    with open(file) as f:
        return f.read()

def get_word_count(content):
    return len(content.split())

def get_letter_count(content):
    letters_count = {}

    for letter in content:
        if not letter.isalpha():
            continue
        if letter.lower() in letters_count.keys():
            letters_count[letter.lower()] += 1
            continue
        
        letters_count[letter.lower()] = 1

    return letters_count

def sort_dictionary(dictionary):
    keys = list(dictionary.keys())
    keys.sort()

    return {i: dictionary[i] for i in keys}

main()
