x = 112
y = 42

if x > y:
    print('x > y: x is {} and y is {}'.format(x,y))
elif x < y:
    print('x < y: x is {} and y is {}'.format(x,y))
elif x == y:
    print('x == y: x is {} and y is {}'.format(x,y))
else:
    print('do something else')


if x == 5: # Python does not have a switch or a case statement because you can do the exact same thing with a string of elif
    print('do five stuff')
elif x == 6:
    print('do six stuff')
elif x == 7:
    print('do seven stuff')
elif x == 8:
    print('do eight stuff')
elif x == 42:
    print('do forty-two stuff')
else:
    print('do that other thing')