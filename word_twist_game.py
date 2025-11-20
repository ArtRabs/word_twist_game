import random
import collections

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

def scramble_word(word):
    word_list = list(word)
    scrambled = "".join(word_list)

    while scrambled == word:
        random.shuffle(word_list)
        scrambled = "".join(word_list)

    return scrambled

def is_valid_word(submission, original_scrambled_word, dictionary_words, guessed_words):

    submission = submission.strip().lower()

    if not submission.isalpha():
        return False, "Invalid input. Please enter only letters."
    
    if submission in guessed_words:
        return False, "Invalid input. You've already guessed that word!"
    
    if submission not in dictionary_words:
        return False, f"'{submission}' iss not in our dictionary."
    
    submission_counts = collections.Counter(submission)
    scrambled_counts = collections.Counter(original_scrambled_word)

    for char, count in submission_counts.items():
        if count > scrambled_counts.get(char,0):
            return False, f"'{submission}' uses letters not available in '{original_scrambled_word}' (or too many of them)."

    return True, "Correct!"

def calculate_score(word):
    return len(word)

def main():
    print("Hello World")

if __name__ == "__main__":
    main()