import turtle
import pandas

screen = turtle.Screen()
screen.title("U. S. States Game")
image = "./day-25/us-states-game/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./day-25/us-states-game/50_states.csv")
all_states = data.state.to_list()
total = len(data)
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/{total}", prompt="Type another state: (type 'exit' for quit.)").title()
    if answer_state in all_states and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
    
    if answer_state == "Exit":
        break

print(f"You guessed {len(guessed_states)} from 50.")


states_to_learn = [state for state in all_states if state not in guessed_states]
# for state in all_states:
#     if state not in guessed_states:
#         states_to_learn.append(state)
print(len(states_to_learn))
new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("./day-25/us-states-game/states_to_learn.csv")





