import random
import collections
import time

# Settings
# You can change the values of these variables

MIN_WORD_LENGTH = 4
MAX_WORD_LENGTH = 7
ROUND_TIME_LIMIT = 60

# start_time = time.time()

# while time.time() - start_time < ROUND_TIME_LIMIT:

#     elapsed_time = time.time() - start_time
#     remaining_time = ROUND_TIME_LIMIT - elapsed_time

def load_words(filename="words.txt"):

    dictionary_words = set()
    selectable_words = []

    try:

        with open(filename, "r") as file:

            for line in file:

                word = line.strip().lower()
                if MIN_WORD_LENGTH <= len(word) <= MAX_WORD_LENGTH and word.isalpha():

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
        return False, f"'{submission}' is not in our dictionary."
    
    submission_counts = collections.Counter(submission)
    scrambled_counts = collections.Counter(original_scrambled_word)

    for char, count in submission_counts.items():
        if count > scrambled_counts.get(char,0):
            return False, f"'{submission}' uses letters not available in '{original_scrambled_word}' (or too many of them)."

    return True, "Correct!"

def calculate_score(word):
    return len(word)

def play_round(dictionary_words, selectable_words):

    total_score = 0
    guessed_words_in_round = set()

    chosen_word = random.choice(selectable_words)
    scrambled_display = scramble_word(chosen_word)

    print("\n--- NEW ROUND --")
    print(f"Scrambled word is: {scrambled_display}")
    print(f"You have {ROUND_TIME_LIMIT} seconds to find words!")
    print("Type 'quit' to end the round early.")

    start_time = time.time()

    while True:

        elapsed_time = time.time() - start_time
        remaining_time = ROUND_TIME_LIMIT - elapsed_time

        if remaining_time <= 0:
            print("\nTime's up!")
            break

        print(f"\nRemaining time: {int(remaining_time)} seconds")
        player_guess = input("Your guess: ").strip().lower()

        if player_guess == "quit":
            print("Exiting round early.")
            break

        is_valid, feedback = is_valid_word(player_guess, scrambled_display, dictionary_words, guessed_words_in_round)

        if is_valid:
            guessed_words_in_round.add(player_guess)
            score = calculate_score(player_guess)
            total_score = total_score + score
            print(f"Correct! Your scored {score} points. Total: {total_score}")
        else:
            print(f"Invalid guess. {feedback}")

    print("\n--- ROUND OVER ---")
    print(f"The original word was: '{chosen_word}'")
    print(f"Total score: {total_score}")

    if guessed_words_in_round:

        print("Words you found:")

        for word in sorted(list(guessed_words_in_round)):

            print(f"- {word}")

    else:

        print("You didn't find any words this round.")
    
    return total_score

def main():
    
    print("Welcome to Word Twist!")
    dictionary_words, selectable_words = load_words()

    if not selectable_words:
        print("No suitable words loaded. Exiting.")
        return
    
    final_score = play_round(dictionary_words, selectable_words)
    
    print("\n--- GAME OVER ---")
    print(f"Your final score: {final_score}")

if __name__ == "__main__":
    main()