# Settings
# You can change the values of these variables

MIN_WORD_LENGTH = 4
MAX_WORD_LENGTH = 7

def load_words(filename="words.txt"):

    dictionary_words = set()
    selectable_words = []

    try:

        with open(filename, "r") as file:

            for line in file:

                word = line.strip().lower()
                if MIN_WORD_LENGTH <= len(word) <= MAX_WORD_LENGTH and word.isalpha:

                    dictionary_words.add(word)
                    selectable_words.append(word)

        print(f"Loaded {len(dictionary_words)} words from '{filename}'.")

    except FileNotFoundError:

        print(f"Error: The word list file '{filename}' was not found.")
        print("Please ensure 'words.txt' in in the same directory as this script.")
        
        exit()

    return dictionary_words, selectable_words

def main():
    print("Hello World")

if __name__ == "__main__":
    main()