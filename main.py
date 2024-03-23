import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].tolist()

guessed_states_list = []

while len(guessed_states_list) <= 50:

    answer_state = screen.textinput(title=f"{len(guessed_states_list)}/50 States Correct", prompt="What's another state name?").title()

    if answer_state == "Exit":
        break

    if answer_state in states_list:

        guessed_states_list.append(answer_state)

        write_turtle = turtle.Turtle()
        write_turtle.hideturtle()
        write_turtle.penup()

        complete_row = data[data['state'].str.contains(answer_state)]
        # complete_row.
        for row in complete_row.itertuples():
            write_turtle.setposition(row.x, row.y)
        write_turtle.pendown()
        write_turtle.write(answer_state)

# states to learn .csv
# print(data["state"])

list_without_guesses = list(set(data["state"]) - set(guessed_states_list))
df = pandas.DataFrame(list_without_guesses)
df.to_csv('missing_states.csv', index=False)




