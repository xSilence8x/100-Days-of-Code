# Phonetic Alphabet Converter

This Python program converts words or phrases into their corresponding NATO phonetic alphabet code words. The NATO phonetic alphabet is used to spell out letters or communicate information clearly and unambiguously.

## Usage

1. Make sure you have Python 3.11 installed on your machine.

2. Clone this repository to your local machine or download the source code.

3. Install the required dependencies.

4. Run the program by executing the `main.py` script.

5. Enter a word or phrase when prompted, and the program will output the corresponding NATO phonetic alphabet code words for each letter.

## Code Overview

- The program uses a CSV file named `nato_phonetic_alphabet.csv`, which contains the mapping between letters and their corresponding code words in the NATO phonetic alphabet.

- The program reads the CSV file using the pandas library and creates a dictionary, `data_dict`, where each letter is mapped to its code word.

- To convert a word or phrase into the NATO phonetic alphabet code, the program takes user input and converts it to uppercase. It then iterates over each letter in the input, retrieves the corresponding code word from `data_dict`, and adds it to the `output` list.

- Finally, the program prints the `output` list, which displays the NATO phonetic alphabet code words for each letter in the input word or phrase.

Input: `Your word: Hello`
Output: `['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']`


