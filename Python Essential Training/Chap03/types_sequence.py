# x = [1, 2, 3, 4, 5]
# x[2] = 42 # A list is a mutable sequence so you can reassign values after they are initially assigned

# x = (1, 2, 3, 4, 5) # A tuple is indicated by parentheses an is immutable
# # x[4] = 42 # Returns an error 

# x = range(5) # It is immutable and starts at 0 and ends at last item - 1
# x = range(5, 50, 5) # Start, stop, step are the arguments for the range function
# x = list(range(5)) # Creates a mutable list for values that range creates
# x[2] = 42

x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5} # A dictionary is a searchable sequence of key value pairs
x['three'] = 42 # Dictionaries are mutable

for i in x: # The for loop sequences through the list and assigns i the value for each value in the list
    print('i is {}'.format(i))

for k, v in x.items(): # Returns a two tuple of each of the items with the key and the value
    print('k: {}, v: {}'.format(k, v))