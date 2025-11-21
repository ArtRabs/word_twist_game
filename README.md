# Word Twist Game in Python

## Table of Contents
-   [Game Overview](#game-overview)
-   [Features](#features)
-   [Project Structure](#project-structure)
-   [Setup and Installation](#setup-and-installation)
-   [How to Play](#how-to-play)
-   [Configuration](#configuration)
-   [Code Structure Highlights](#code-structure-highlights)

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

## Setup and Installation

To run the Word Twist game, you'll need Python installed on your system.
1.  **Save the Code:**
    *   Save the provided Python code (from `word_twist_game.py`) into a file named `word_twist_game.py`.
2.  **Create the Word List:**
    *   In the *same directory* as `word_twist_game.py`, create a new plain text file named `words.txt`.
    *   Populate or generate `words.txt` with words, one word per line. Ensure words are in lowercase and consist only of letters.
    *   (Note: There is a given `words.txt` that can be used as a sample)
3.  **Run the Game:**
    *   There are more than one way to run the game.
    *   1. Open your terminal or command prompt.
    *   Navigate to the directory where you saved `word_twist_game.py` and `words.txt`.
    *   Execute the game using the command:
        ```bash
        python word_twist_game.py
        ```
    *   2. Open your preferred IDE like Visual Studio Code or Pycharm.
    *   Open file `word_twist_game.py` where both `word_twist_game.py` and `words.txt` are in the same directory.
    *   Run the Python file in dedicated terminal.

## How to Play

1.  The game will start by displaying a scrambled word and a time limit.
2.  Type your guesses at the prompt.
3.  Press `Enter` after each guess.
4.  The game will provide feedback on whether your guess is correct, already guessed, not in the dictionary, or uses invalid letters.
5.  Points are awarded for each valid word found.
6.  The round ends when the time limit expires or you type `quit`.
7.  A summary of your score and found words will be displayed at the end of the round.

## Configuration

You can easily customize game parameters by modifying the constants at the top of `word_twist_game.py`:
```python
MIN_WORD_LENGTH = 4      # Minimum length for words loaded from file
MAX_WORD_LENGTH = 7      # Maximum length for words loaded from file
ROUND_TIME_LIMIT = 60    # Time limit for the round in seconds

load_words(): Handles reading and filtering words from words.txt.
scramble_word(): Randomizes the letters of a chosen word.
is_valid_word(): Contains all logic for checking player submissions against the dictionary and scrambled letters.
calculate_score(): Determines points for a valid word.
play_round(): Manages the main game loop, time limit, and round flow.
main(): The entry point orchestrating the game setup and execution.