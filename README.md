# Word Twist Game in Python

## Game Overview

The Word Twist game presents players with a set of scrambled letters derived from a secret word. The objective is to guess as many valid English words as possible using *only* the available letters within a set time limit. Points are awarded based on the length of correctly guessed words.

## Features

*   **Random Word Selection:** Picks a word from a predefined `words.txt` list.
*   **Word Scrambling:** Randomly shuffles the letters of the chosen word, ensuring it's different from the original.
*   **User Input Handling:** Prompts the player for guesses and handles various input scenarios.
*   **Robust Word Validation:**
    *   Checks if the guessed word exists in the loaded dictionary.
        *   Verifies that the guessed word uses only letters available in the scrambled word, and not more times than they appear.
    *   Prevents duplicate guesses within a round.
*   **Scoring System:** Awards points based on word length.
*   **Time Limit:** Ends the round after a configurable duration, creating a challenging pace.
*   **Detailed User Feedback:** Provides clear messages for invalid inputs, correct guesses, time remaining, and round summaries.
*   **Configurable Settings:** Easily adjust word length constraints and round time limits.

## Project Structure

The project maintains a simple structure for ease of use:
word_twist_project/ 
├── word_twist_game.py # Main Python script containing all game logic 
└── words.txt # Text file storing the dictionary of words