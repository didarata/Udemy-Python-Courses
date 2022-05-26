# Lists can be thought of the most general version of a sequence in Python. Unlike strings, they are mutable,
# meaning the elements inside a list can be changed!

my_list = ['A string',23,100.232,'o']
print(len(my_list))

my_list = ['one','two','three',4,5]
print(my_list[0])                       # Grab element at index 0
print(my_list[1:])                      # Grab index 1 and everything past it
print(my_list[:3])                      # Grab everything UP TO index 3
my_list = my_list + ['new item']        # We can also use + to concatenate lists, just like we did for strings.
print(my_list)                          # Reassign
my_list = my_list * 2                   # Make the list double
print(my_list)


list1 = [1, 2, 3]                        # Create a new list
list1.append('append me!')               # Append
print(list1)
list1.pop(0)                             # Pop off the 0 indexed item
popped_item = list1.pop()                # Assign the popped element, remember default popped index is -1
print(popped_item)
print(list1)

new_list = ['a','e','x','b','c']
print(new_list)
new_list.reverse()                       # Use reverse to reverse order (this is permanent!)
print(new_list)
new_list.sort()                          # Use sort to sort the list (in this case alphabetical order, but for numbers it will go ascending)
print(new_list)

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]
matrix = [lst_1, lst_2, lst_3]           # Make a list of lists to form a matrix
print(matrix)
print(matrix[0])                         # Grab first item in matrix object
print(matrix[0][0])                      # Grab first item of the first item in the matrix object