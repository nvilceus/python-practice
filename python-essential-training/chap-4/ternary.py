# Ternary does not work in versions of Python previous to Python 2.5

hungry = False
# x = 'Feed the bear now!' if hungry else 'Do not feed the bear.' # Need both if and else clauses to use the ternary operator
x = 'Feed the bear now!' if hungry else None
print(x)