import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def type_of_game(type):
    """Takes user's input of difficulty type and returns number of attempts"""
    if type == "easy":
        return EASY_LEVEL_ATTEMPTS, f"You have 10 attempts remaining to guess the number."
    else:
        return HARD_LEVEL_ATTEMPTS, f"You have 5 attempts remaining to guess the number."


def game():
    print(f"Welcome to the Number Guessing Game!")
    print(f"I am thinking of a nnumber between 1 and 100.")

    secret_number = random.randint(1, 100)
    guess = 0

    difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard': ").lower()

    attempts, message = type_of_game(difficulty)
    print(message)

    while guess != secret_number:
        guess = int(input(f"Make a guess: "))
        if guess == secret_number:
            print(f"You gussed the number! Congratulations!")
            
        else:
            if guess < secret_number:
                print(f"Too low.")
            else:
                print(f"Too high.")
            attempts -= 1
            print(f"Number of remaining attempts: {attempts}")
        
        if attempts < 1:
            print(f"You lose! The number was {secret_number}")
            return
        elif guess != secret_number:
            print(f"Guess again.")

game()
