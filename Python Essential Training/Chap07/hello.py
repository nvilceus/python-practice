def f1(f):
    def f2():
        print('this is before the funciton call')
        f()
        print('this is after the function call')
    return f2

@f1 # Decorator takes the function defined directly after it and passes it to the decorator function. Assigns the name of f3 to a wrapper
def f3():
    print('this is f3')

f3()