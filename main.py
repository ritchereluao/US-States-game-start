import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=725, height=491)

data = pandas.read_csv("50_states.csv")

data_in_list = data["state"].tolist()
correct_answer = 0
game_is_on = True

while game_is_on:

    answer_state = screen.textinput(title=f"{correct_answer}/50 States Correct", prompt="What's another state name?")
    answer_state = answer_state.title()

    if answer_state in data_in_list:

        x = data[data["state"] == answer_state].x.item()
        y = data[data["state"] == answer_state].y.item()

        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x, y)
        writer.write(answer_state, align="center", font=("Arial", 8, "bold"))

        correct_answer += 1
        data_in_list.remove(answer_state)

        if correct_answer == 50:
            game_is_on = False

screen.exitonclick()
