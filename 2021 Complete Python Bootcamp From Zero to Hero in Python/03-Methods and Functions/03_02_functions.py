# What is a function?
# Formally, a function is a useful device that groups together a set of statements so they can be run more than once. They
# can also let us specify parameters that can serve as inputs to the functions.
# On a more fundamental level, functions allow us to not have to repeatedly write the same code again and again. If you
# remember back to the lessons on strings and lists, remember that we used a function len() to get the length of a string.
# Since checking the length of a sequence is a common task you would want to write a function that can do this repeatedly at command.
# Functions will be one of most basic levels of reusing code in Python, and it will also allow us to start thinking of
# program design (we will dive much deeper into the ideas of design when we learn about Object Oriented Programming).

# def name_of_function(arg1,arg2):
    # '''
    # This is where the function's Document String (docstring) goes.
    # When you call help() on your function it will be printed out.
    # '''
    # Do stuff here
    # Return desired result

def say_hello():
    print('hello')


say_hello()


def greeting(name):
    print(f'Hello {name}')


greeting('Miro')


def add_num(num1,num2):
    return num1+num2


print(add_num(4, 5))
# Can also save as variable due to return
result = add_num(4, 5)
print(result)

# What happens if we input two strings?
print(add_num('one', 'two'))


# Very Common Question: "What is the difference between return and print?"
# The return keyword allows you to actually save the result of the output of a function as a variable. The print() function
# simply displays the output to you, but doesn't save it for future use. Let's explore this in more detail

def print_result(a, b):
    print(a + b)


print_result(10, 5)


def return_result(a, b):
    return a + b


# You won't see any output if you run this in a .py script
return_result(10, 5)

# But what happens if we actually want to save this result for later use?
my_result = print_result(20, 20)
print(my_result)
# Be careful! Notice how print_result() doesn't let you actually save the result to a variable! It only prints it out,
# with print() returning None for the assignment!
my_result = return_result(20, 20)
print(my_result)
print(my_result + my_result)


def even_check(number):
    return number % 2 == 0


print(even_check(20))
print(even_check(21))


# Check if any number in a list is even
def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Otherwise we don't do anything
        else:
            pass


print(check_even_list([1, 2, 3]))
print(check_even_list([1, 1, 1]))


# VERY COMMON MISTAKE!! LET'S SEE A COMMON LOGIC ERROR, NOTE THIS IS WRONG!!!
def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # This is WRONG! This returns False at the very first odd number!
        # It doesn't end up checking the other numbers in the list!
        else:
            return False


# UH OH! It is returning False after hitting the first 1
print(check_even_list([1, 2, 3]))


# Correct Approach: We need to initiate a return False AFTER running through the entire loop
def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop
    return False


print(check_even_list([1,2,3]))
print(check_even_list([1,3,5]))


# Return all even numbers in a list
def check_even_list(num_list):
    even_numbers = []

    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we append the even number
        if number % 2 == 0:
            even_numbers.append(number)
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop
    return even_numbers


print(check_even_list([1, 2, 3, 4, 5, 6]))
print(check_even_list([1, 3, 5]))

# Returning Tuples for Unpacking

stock_prices = [('AAPL', 200), ('GOOG', 300), ('MSFT', 400)]
for item in stock_prices:
    print(item)

for stock, price in stock_prices:
    print(stock)
    print(price)

# Similarly, functions often return tuples, to easily return multiple results for later use.

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]


def employee_check(work_hours):
    # Set some max value to intially beat, like zero hours
    current_max = 0
    # Set some empty value before the loop
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    # Notice the indentation here
    return (employee_of_month, current_max)


print(employee_check(work_hours))

# Interactions between functions

example = [1,2,3,4,5]
from random import shuffle
# Note shuffle is in-place
shuffle(example)
print(example)

# OK, let's create our simple game

mylist = [' ','O',' ']
def shuffle_list(mylist):
    # Take in list, and returned shuffle versioned
    shuffle(mylist)

    return mylist


print(mylist)
print(shuffle_list(mylist))


def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        # Recall input() returns a string
        guess = input("Pick a number: 0, 1, or 2:  ")

    return int(guess)


player_guess()


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)


# Initial List
mylist = [' ','O',' ']

# Shuffle It
mixedup_list = shuffle_list(mylist)

# Get User's Guess
guess = player_guess()

# Check User's Guess
#------------------------
# Notice how this function takes in the input
# based on the output of other functions!
check_guess(mixedup_list,guess)