a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'

# if 'leaf' in x:
#     print('expression is true')
# else:
#     print('expression is false')

# if y is x[0]: # Strings are not muteable so y and x[0] are the same object
#     print('expression is true')
# else:
#     print('expression is false')

if y is not x[1]:
    print('expression is true')
else:
    print('expression is false')

print(id(y))
print(id(x[0]))