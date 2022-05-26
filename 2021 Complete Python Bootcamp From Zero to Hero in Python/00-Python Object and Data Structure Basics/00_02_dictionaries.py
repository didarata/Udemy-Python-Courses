# So what are mappings? Mappings are a collection of objects that are stored by a key, unlike a sequence that stored
# objects by their relative position. This is an important distinction, since mappings won't retain order since they
# have objects defined by a key.
# A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.

my_dict = {'key1':'value1','key2':'value2'}             # Make a dictionary with {} and : to signify a key and a value
print(my_dict)
print(my_dict['key2'])                                  # Call values by their key

# Its important to note that dictionaries are very flexible in the data types they can hold. For example:
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict)
print(my_dict['key3'])                                  # Let's call items from the dictionary
print(my_dict['key3'][0])                               # Can call an index on that value
print(my_dict['key3'][0].upper())                       # Can then even call methods on that value

print(my_dict['key1'])
my_dict['key1'] = my_dict['key1'] - 123                 # Subtract 123 from the value
print(my_dict)
my_dict['key1'] -= 123                                  # Set the object equal to itself minus 123
print(my_dict['key1'])

# We can also create keys by assignment. For instance if we started off with an empty dictionary, we could continually add to it:
d = {}                                                  # Create a new dictionary
d['animal'] = 'Dog'                                     # Create a new key through assignment
print(d)
d['answer'] = 42                                        # Can do this with any object
print(d)

d = {'key1': 1, 'key2': 2, 'key3': 3}                        # Create a typical dictionary
print(d.keys())                                         # Method to return a list of all keys
print(d.values())                                       # Method to grab all values
print(d.items())                                        # Method to return tuples of all items  (we'll learn about tuples soon)