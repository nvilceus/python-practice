x = 42
print('Hello, World. {}'.format(x)) # {} is a placeholder
s = 'Hello, World. {}'.format(x) # Format() is a method of the string object
print(s)

print('Hello, World. %d' % x) # % x replaces %d like in the C language
print(f'Hello, World. {x}') # Another way to format in Python 3.6 and later versions