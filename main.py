import turtle
import pandas as pd
from states import State
import csv

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states = pd.read_csv("50_states.csv")
correct_guesses = []
score = 0

game_is_on = True
while game_is_on:

    answer_state = screen.textinput(title=f"{score}/50 states correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states.state:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if (all_states.state == answer_state).any() and answer_state not in correct_guesses:
        state_row = all_states[all_states.state == answer_state]
        state = State(answer_state, state_row.x.item(), state_row.y.item())
        correct_guesses.append(answer_state)
        score += 1

    if len(correct_guesses) >= 50:
        game_is_on = False

