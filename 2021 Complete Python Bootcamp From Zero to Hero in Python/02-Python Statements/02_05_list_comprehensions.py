mystring = 'hello'

mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)


# Grab every letter in string
lst = [x for x in 'word']
print(lst)

# Square numbers in range and turn into list
lst = [x**2 for x in range(0,11)]
print(lst)

# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]
print(lst)

# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius ]
print(fahrenheit)


lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)

# if else statement in one line, bad readability so never use it in real  world.
results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

# nested loop in comprehension but dont use, take it easy for readability

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)