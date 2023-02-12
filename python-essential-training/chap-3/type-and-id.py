# x = (1, 2, 3, 4, 5)
x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)

print('x is {}'.format(x))
print(type(x))
print(type(x[1]))
print('{}\n'.format(type(y[1])))

print(id(x)) # Id function returns a unique identifier for each object
print(id(y))
if x is y: # Not the same object even though they have all the same values 
    print('yep\n')
else:
    print('nope\n')

# Prints the same thing because there is only one literal number 1 object
print(id(x[0]))
print(id(y[0]))

if x[0] is y[0]: # Use the is operator to check if two objects are the same object
    print('yep\n')
else:
    print('nope\n')

if isinstance(x, tuple): # Use isinstance() to check if a variable is a certain type
    print('x is a tuple\n')
elif isinstance(x, list):
    print('x is a list\n')
else:
    print('x is neither a tuple or list\n')

y = [1, 'two', 3.0, [4, 'four'], 5]
if isinstance(y, tuple):
    print('y is a tuple\n')
elif isinstance(y, list):
    print('y is a list\n')
else:
    print('y is neither a tuple or list\n')