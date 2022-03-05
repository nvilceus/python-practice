# Can use triple quotes for a multi-line string
# x = """ 
# seven""" 

# x = 'seven'.capitalize() # Capitalizes the s in seven
# x = 'Seven'.lower() # Makes the S in seven lowercase

# x = 'seven {} {}'.format(8, 9)
# x = 'seven {1} {0}'.format(8, 9) # Swaps the 8 and 9
# x = 'seven {1:<9} {0:>9}'.format(8, 9) # Puts eight spaces to the right of 9 and eight spaces to the left of 8
# x = 'seven "{1:<9}"" "{0:>9}"'.format(8, 9) # Puts quotes around the 9 and its spaces as well as the 8 and its spaces
# x = 'seven "{1:<09}"" "{0:>09}"'.format(8, 9) # Fills in the spaces after the 9 and the spaces before the 8 with 0s 
# x = 'seven "{1:<09}"" "{0:>09}"'.format(8, 12345) # Fills in five of the nine total spaces with 12345

# x = 'seven {} {}' # If this variable is printed the brackets will be printed when not using format()

a = 8
b = 9
# x = f'seven {a} {b}' # This is formatting using an f string for Python 3.6 and afterward
x = f'seven {a:<09} {b:>09}'

print('x is {}'.format(x))
print(type(x))
