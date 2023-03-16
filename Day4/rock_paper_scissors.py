import random

print(100 * "#", "\n\n\tWelcome to my Paper, Rock, Scissors GAME!!!\n\n",100 * "#")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

play = {0: rock, 1: paper, 2: scissors}

while True:
    # handle ValueError and KeyError using try and except
    try: 
        user = int(input("Choose 0 for Rock, 1 for Paper or 2 for Scissors: "))
        print(f"You chose: {play[user]}")
        
        computer = random.randint(0, 2)
        print(f"Computer chose: {play[computer]}")

        # stringify obtained inputs from user and computer   
        game = str(user) + str(computer)

        # define what is draw and win situation
        draw = ["00", "11", "22"]
        loose = ["20", "01", "12"]

        if game in draw:
            print(f"This ended in a draw!")
        elif game in loose:
            print(f"You loose!")
        else:
            print(f"You win!")
        answer = input("Another game? Type \"N\" for end otherwise press any ")
        
        # ask for new round or end the game
        if isinstance(answer, str) & (answer.upper() == "N"):
            break
    except ValueError:
        print("You did not type number!")
    except KeyError:
        print("You did not choose number from 0 to 2!")
