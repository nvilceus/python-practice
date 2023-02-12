from decimal import * # * imports everything from decimal so no need for decimal.Decimal() below

# x = 7 * 3 # Class int
# x = 7.0 # Class float
# x = 7 * 3.14159 # Class float
# x = 7 / 3 # Class float because Python 3 stopped doing integer division
# x = 7 // 3 # Class int because // operator does integer division in Python 3
# x = 7 % 3 # Class int and gives the remainder of 7/3

# Have to use the class Decimal when dealing with money because of floating point errors 
# x = .1 + .1 + .1 - .3 # Class float and not 0 which is a problem with Python because of sacrificing accuracy for precision
a = Decimal('.10') # Want to pass decimal a string instead of a float for accuracy
b = Decimal('.30')
x = a + a + a - b # Class decimal.Decimal type so the Decimal class from the decimal library

print('x is {}'.format(x))
print(type(x))
