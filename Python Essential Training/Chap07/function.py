# def main():
#     x = kitten()
#     print(x)

# def kitten():
#     return 'Meow.'

# if __name__ == '__main__': main() # Standard for Python which does not have forward declarations

# def main():
#     kitten(5)

# def kitten(a, b = 1, c = 0): # Including a d with no defaul will give syntax error because arguments with defaults must be at the end of the list
#     print('Meow.')
#     print(a, b, c)

# if __name__ == '__main__': main()

# def main():
#     # x = 5
#     x = [5]
#     kitten(x)
#     print(f'in main: x is {x}')

# def kitten(a): # Function arguments act as assignments in Python
#     # a = 3 # Call by value does not change the value of the original immutable integer
#     a[0] = 3 # Call by reference changes the value in the original mutable list too
#     print(a)

# if __name__ == '__main__': main()

def main():
    x = kitten()
    print(type(x), x)

def kitten(): 
    print('Meow.')
    return dict(x = 42, y = 43, z = 44)

if __name__ == '__main__': main()