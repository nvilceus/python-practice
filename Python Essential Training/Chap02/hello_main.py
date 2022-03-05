import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version())) 
    print('line 2')
    if False:
        print('line 3')
    else:
        print('not true')

if __name__ == '__main__': main() # Forces the interpreter to read the entire script before it executes any code