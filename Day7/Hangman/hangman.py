# Python 🐍 Hangman GAME
import random
import logo
import stages

print(logo.hangman_logo)
print(logo.about)

# you can have any list of your words
my_words = ["apple", "teacher", "duck", "goose", "mouse"]

# generate random word and make it secret in display_secret as "_ _ _ _"
my_secret_word = random.choice(my_words)
my_secret_word_list = [char for char in my_secret_word]
display_secret = ["_" for char in my_secret_word]

length = len(my_secret_word)

end_of_game = False
number_of_lives = 6 
print(f"{' '.join(display_secret)}")

while not end_of_game:
    user_guess = input("Guess a character: ").lower()

    if user_guess in display_secret:
        print(f"You have already guessed {user_guess}! Try another one.")
    else:
        for n in range(length):
            if user_guess == my_secret_word_list[n]:
                display_secret[n] = user_guess
    
    print(f"{' '.join(display_secret)}")

    if user_guess not in my_secret_word_list:
        number_of_lives -= 1
        print(stages.stages[number_of_lives])
        print(f"Number of your remaining lives: {number_of_lives}")
        if number_of_lives == 0:
            print(stages.stages[0])
            print(f"Game over! You lose! \n The secret word was: {my_secret_word}")
            end_of_game = True

    
    if not "_" in display_secret:
        end_of_game = True
        print("You won the game! Congratulations!")
