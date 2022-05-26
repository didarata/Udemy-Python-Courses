from IPython.display import clear_output
# It is time to get you to put together all your skills to start building usable projects! Before you jump into our full milestone project,
# we will go through some warm-up component exercises, to get you comfortable with a few key ideas we use in the milestone project and
# larger projects in general, specifically:
#
# Getting User Input
# Creating Functions that edit variables based on user input
# Generating output
# Joining User Inputs and Logic Flow

def display_list(mylist):
    print(mylist)


mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
display_list(mylist)

input('Please enter a value: ')
result = input("Please enter a number: ")


def user_choice():
    """
    User inputs a number (0-10) and we return this in integer form.
    No parameter is passed when calling this function.
    """
    choice = input("Please input a number (0-10)")

    return int(choice)


some_input = '10'
# Lot's of .is methods availble on string
some_input.isdigit()


def user_choice():
    # This original choice value can be anything that isn't an integer
    choice = 'wrong'

    # While the choice is not a digit, keep asking for input.
    while choice.isdigit() == False:
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Choose a number: ")

    # We can convert once the while loop above has confirmed we have a digit.
    return int(choice)


def user_choice():
    # This original choice value can be anything that isn't an integer
    choice = 'wrong'

    # While the choice is not a digit, keep asking for input.
    while choice.isdigit() == False:

        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Choose a number: ")

        # Error Message Check
        if choice.isdigit() == False:
            print("Sorry, but you did not enter an integer. Please try again.")

    # We can convert once the while loop above has confirmed we have a digit.
    return int(choice)


clear_output()


def user_choice():
    # This original choice value can be anything that isn't an integer
    choice = 'wrong'

    # While the choice is not a digit, keep asking for input.
    while choice.isdigit() == False:

        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Choose a number: ")

        if choice.isdigit() == False:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_output()

            print("Sorry, but you did not enter an integer. Please try again.")

    # Optionally you can clear everything after running the function
    # clear_output()

    # We can convert once the while loop above has confirmed we have a digit.
    return int(choice)


def user_choice():
    choice = 'WRONG'
    within_range = False

    while choice.isdigit() == False or within_range == False:

        choice = input("Please enter a number (0-10): ")

        if choice.isdigit() == False:
            print("Sorry that is not a digit!")

        if choice.isdigit() == True:
            if int(choice) in range(0, 10):
                within_range = True
            else:
                within_range = False

    return int(choice)


game_list = [0, 1, 2]


def display_game(game_list):
    print("Here is the current list")
    print(game_list)


def position_choice():
    # This original choice value can be anything that isn't an integer
    choice = 'wrong'

    # While the choice is not a digit, keep asking for input.
    while choice not in ['0', '1', '2']:

        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Pick a position to replace (0,1,2): ")

        if choice not in ['0', '1', '2']:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_output()

            print("Sorry, but you did not choose a valid position (0,1,2)")

    # Optionally you can clear everything after running the function
    # clear_output()

    # We can convert once the while loop above has confirmed we have a digit.
    return int(choice)


def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at the position")

    game_list[position] = user_placement

    return game_list


def gameon_choice():
    # This original choice value can be anything that isn't a Y or N
    choice = 'wrong'

    # While the choice is not a digit, keep asking for input.
    while choice not in ['Y', 'N']:

        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Would you like to keep playing? Y or N ")

        if choice not in ['Y', 'N']:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_output()

            print("Sorry, I didn't understand. Please make sure to choose Y or N.")

    # Optionally you can clear everything after running the function
    # clear_output()

    if choice == "Y":
        # Game is still on
        return True
    else:
        # Game is over
        return False


# Variable to keep game playing
game_on = True

# First Game List
game_list = [0, 1, 2]

while game_on:
    # Clear any historical output and show the game list
    clear_output()
    display_game(game_list)

    # Have player choose position
    position = position_choice()

    # Rewrite that position and update game_list
    game_list = replacement_choice(game_list, position)

    # Clear Screen and show the updated game list
    clear_output()
    display_game(game_list)

    # Ask if you want to keep playing
    game_on = gameon_choice()
