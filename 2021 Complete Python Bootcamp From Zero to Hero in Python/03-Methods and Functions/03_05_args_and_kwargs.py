# # *args and **kwargs
# # Work with Python long enough, and eventually you will encounter *args and **kwargs. These strange terms show up as
# # parameters in function definitions. What do they do? Let's review a simple function:

# def myfunc(a,b):
#     return sum((a,b))*.05


# print(myfunc(40,60))


# def myfunc(a=0,b=0,c=0,d=0,e=0):
#     return sum((a,b,c,d,e))*.05


# print(myfunc(40,60,20))

# # Obviously this is not a very efficient solution, and that's where *args comes in.
# #
# # *args
# # When a function parameter starts with an asterisk, it allows for an arbitrary number of arguments, and the function
# # takes them in as a tuple of values. Rewriting the above function:


# def myfunc(*args):
#     return sum(args)*.05


# print(myfunc(40,60,20))


# def myfunc(*spam):
#     return sum(spam)*.05


# print(myfunc(40,60,20))


# # **kwargs
# # Similarly, Python offers a way to handle arbitrary numbers of keyworded arguments. Instead of creating a tuple of
# # values, **kwargs builds a dictionary of key/value pairs. For example:


# def myfunc(**kwargs):
#     if 'fruit' in kwargs:
#         print(
#             f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
#     else:
#         print("I don't like fruit")


# print(myfunc(fruit='pineapple'))
# print(myfunc())


# # *args and **kwargs combined
# # You can pass *args and **kwargs into the same function, but *args have to appear before **kwargs


# def myfunc(*args, **kwargs):
#     if 'fruit' and 'juice' in kwargs:
#         print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
#         print(f"May I have some {kwargs['juice']} juice?")
#     else:
#         pass


# print(myfunc('eggs', 'spam', fruit='cherries', juice='orange'))

# # Placing keyworded arguments ahead of positional arguments raises an exception:
# # print(myfunc(fruit='cherries',juice='orange','eggs','spam'))

# # As with "args", you can use any name you'd like for keyworded arguments - "kwargs" is just a popular convention.
# #
# # That's it! Now you should understand how *args and **kwargs provide the flexibilty to work with arbitrary numbers of arguments!
