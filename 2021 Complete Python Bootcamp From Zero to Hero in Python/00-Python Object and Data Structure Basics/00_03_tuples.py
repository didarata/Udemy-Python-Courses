# In Python tuples are very similar to lists, however, unlike lists they are immutable meaning they can not be changed.
# You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar.

t = (1, 2, 3)                                             # Create a tuple
print(len(t))                                             # Check len just like a list

t = ('one', 2)                                            # Can also mix object types
print(t)
print(t[0])                                               # Use indexing just like we did in lists
print(t[-1])                                              # Slicing just like a list

print(t.index('one'))                                     # Use .index to enter a value and return the index
print(t.count('one'))                                     # Use .count to count the number of times a value appears

# It can't be stressed enough that tuples are immutable. To drive that point home:

t[0]= 'change'                                            # ERROR
t.append('nope')                                          # ERROR

# You may be wondering, "Why bother using tuples when they have fewer available methods?" To be honest,
# tuples are not used as often as lists in programming, but are used when immutability is necessary.
# If in your program you are passing around an object and need to make sure it does not get changed,
# then a tuple becomes your solution. It provides a convenient source of data integrity.


