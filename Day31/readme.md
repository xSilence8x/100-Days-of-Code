# Flash Cards

This script creates a flashcard application using the Tkinter library in Python. It allows you to learn and practice vocabulary words by displaying French and English translations on flashcards.

## Requirements

- Python 3.11
- Tkinter library
- pandas library

## Installation

1. Clone the repository or download the script files.
2. Install the required libraries using pip:
3. Run the script.

## Usage

1. The script reads the word data from a CSV file. If the file "words_to_learn.csv" exists, it will be used. Otherwise, the file "french_words.csv" will be used as a fallback.
2. The flashcard application is displayed, showing a flashcard with the French word and a button to indicate whether you answered correctly or incorrectly.
3. Click the "Right" button if you answered correctly, or the "Wrong" button if you answered incorrectly.
4. After 3 seconds, the flashcard flips to show the English translation.
5. The word is removed from the list of words to learn if answered correctly. The updated list is saved in the "words_to_learn.csv" file.

## File Structure

- `flash_cards.py`: The main script file.
- `data/`: Directory containing the CSV files with word data.
- `images/`: Directory containing the card images used in the application.

## Screenshots


