import game_data
import random
import art

print(art.logo)

def pick_two_facts(game_data, score, previous):
    """Randomly chooses 2 facts from data and returns them."""
    line_a = random.choice(game_data)
    line_b = random.choice(game_data)
    if score > 0:
        line_a = previous
    while line_a == line_b:
        line_b = random.choice(game_data)
    return line_a, line_b

def compare(a, b):
    """Compares and returns fact with more followers."""
    return "A" if a > b else "B"

def game():
    score = 0
    is_running = True
    previous = {}
    while is_running == True:
        
        compare_a, compare_b = pick_two_facts(game_data.data, score, previous)
        

        print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
        print(art.vs)
        print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")

        result_of_compare = compare(compare_a["follower_count"], compare_b["follower_count"])
        answer = input(f"Who has more followers? 'A' or 'B'? ").upper()

        if (answer == "A" and result_of_compare == "A") or (answer == "B" and result_of_compare == "B"):
            score += 1
            print(f"You are rigth! Current score: {score}")
            previous = compare_b
        else:
            print(f"Sorry, that is wrong. Final score: {score}")
            is_running = False
game()


