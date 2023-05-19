# US States Game

The "US States Game" is a Python project that allows you to play a game where you guess the names of US states, 
and the program marks the correct guesses on a blank map of the United States using the Turtle module. It is written in Python 3.11.

## Installation

To run the "US States Game," please follow these steps:

1. Clone or download the repository to your local machine.
2. Ensure you have Python 3.11 or a compatible version installed.


## Usage

1. Run the `main.py` script to start the game.
2. A blank map of the United States, represented by the `blank_states_img.gif` image, will be displayed. 
3. You will be prompted to guess the names of the US states. 
4. If your guess is correct, the program will mark the state's name on the map. 
5. Keep guessing until you have identified all the states. 
6. At the end of the game, the program will generate a `states_to_learn.csv` file containing the names of the states you missed.

## Project Files

The project repository includes the following files:

- `main.py`: The main script program that runs the "US States Game."
- `blank_states_img.gif`: A GIF image file representing a blank map of the United States.
- `50_states.csv`: A CSV file containing a database of all the US states.
- `states_to_learn.csv`: A CSV file generated at the end of the game, listing the states you missed.

## Game Screenshot

![Game Screenshot](screenshot.png)


## Dependencies

The "US States Game" relies on the following Python packages:

- `turtle`: A built-in module in Python's standard library used for graphics and animations.
- `pandas`: A powerful data manipulation and analysis library for Python.
