import turtle
import pandas
from turtle import Screen

# Initializing screen object (giving it a title and image)
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# Creating an object called 'data' that reads the csv using Python Pandas and selecting the last two columns
data = pandas.read_csv("50_states.csv")
last_two_columns = data.iloc[:, -2:]

# Transform each row into a tuple and create a new DataFrame
tuple_coor = last_two_columns.apply(tuple, axis=1).to_frame('Coordinates')


# Gives 'state_table' a name "States" turns it into a column and merges it with tuple_coor to one table
state_table = data.state.str.lower().to_frame("States")
merged_table = pandas.concat([state_table, tuple_coor], axis=1)

# Creates object 'state_name' that represents the name of the state on the screen
state_name = turtle.Turtle()
state_name.speed(0)

# Creating two lists
state_list = data.state.to_list()
guessed_states = []

# Makes sure the game keeps running
correct_answers = 0
while True:
    # Creating a pop-up on screen that asks you the guess a state
    users_answer = screen.textinput(title=f"{correct_answers}/50 States Correct",
                                    prompt="What's a state's name? ").lower()

    # Checks if the user wants to exit
    if users_answer == "exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Checks if users_answer is in merged_table and then prints it on screen
    if users_answer in merged_table.States.values:
        coordinates = merged_table.loc[merged_table.States == users_answer.lower(), 'Coordinates'].values[0]
        state_name.penup()
        state_name.goto(coordinates)
        state_name.write(users_answer, align="center", font=("Italic", 10, "normal"))
        state_name.hideturtle()

        # Update the count of correct answers and adds users_answer to list guessed_states
        correct_answers += 1
        guessed_states.append(users_answer)

