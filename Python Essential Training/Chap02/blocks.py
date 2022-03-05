x = 42
y = 73

if x < y:
    z = 112 # Blocks do not define scopes in Python (functions, objects, and modules do define scope)
    print('x < y: x is {} and y is {}'.format(x,y))
    print('line 2')
    print('line 3')
 # print('line 4') block need to be indented at the same level

print('z is {}'.format(z))