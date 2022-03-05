class RevStr(str): # inheriting from str which is a built in Python class
    def __str__(self): 
        return self[::-1]

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__': main()