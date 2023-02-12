# x = False
# x = 7 > 5
# x = None # Class NoneType and used to represent the abscence of a value
x = 1

print('x is {}'.format(x))
print(type(x))

if x: # If logical returns false with the value of None, 0 not in a bracket, empty string, or empty bracket
    print("True")
else:
    print("False") 