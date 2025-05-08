import sys
from stats import get_num_words
from stats import get_num_cha
from stats import chars_to_sorted_list

def get_book_text(filepath):
    # Open the file using the filepath parameter
    with open(filepath) as f:
        # Read the contents of the file
        contents = f.read()
    # Return the contents
    return contents

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the file path from command-line arguments
    path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)
    num_words = get_num_words(text)
    count = get_num_cha(text)
    answers = chars_to_sorted_list(count)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in answers:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")

    print("============= END ===============")

if __name__== "__main__":
    main()
