frankenstein_path = "books/frankenstein.txt"

character_dict = {}
length = 0

def count_chars(input):
    for char in input:
        if char not in character_dict and (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90):
            character_dict[char] = 0
        if (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90):
            character_dict[char] += 1

def print_report(len, dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len} words found in the document")
    print("")
    for key in dict:
        print(f"The '{key}' character was found {dict[key]} times")
    print("")
    print("--- End report ---")

def main():
    with open(frankenstein_path) as path:
        file_content = path.read()
        length = len(file_content.split())
        lower_case = file_content.lower()
        count_chars(lower_case)
        print_report(length, character_dict)

main()