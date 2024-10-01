def main():
    path = "books/frankenstein.txt"
    content = get_content(path)
    number_of_words = get_number_of_words(content)
    number_of_each_character = get_number_of_characters(content)
    print_report(path, number_of_words, number_of_each_character)
    

def print_report(path, number_of_words, count_of_characters):
    print(f"--- Report of: {path} ---")
    print(f"{number_of_words} words were found in the document")
    for dict in dict_to_sorted_list(count_of_characters):
        print(f"{dict["character"]}: {dict["count"]}")

def get_content(path):
    with open(path) as f:
        return f.read()


def get_number_of_words(content):
    words = content.split()
    return len(words)

def get_number_of_characters(content):
    character_count = {}
    for char in content.lower():
        if not char.isalpha():
            continue
        
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def dict_to_sorted_list(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"character": ch, "count": dict[ch]})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["count"]

main()