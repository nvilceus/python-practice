def main():
    x = ('meow', 'grrr', 'purr', 'hello', 'world')
    kitten(*x)

def kitten(*args): # Asterik before a variable is the variable length argument list
    if len(args): # Checks if the length is greater than zero
        for s in args:
            print(s)
    else: print('Meow.')   

if __name__ == "__main__": main()    