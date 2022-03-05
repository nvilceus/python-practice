class Duck: # Do not need parantheses in Python 3 because classes automatically inheret the object class
    sound = 'Quaaack!' # Class variable
    walking = 'Walks like a duck.'

    def quack(self): # Self is a reference to the object when the class is used to create an object
        print(self.sound)

    def walk(self): # Self could be any word, but everyone uses self
        print(self.walking)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

    # Other ways to call methods
    Duck().quack() 

    # Was messing around and found out that you can call the quack method using the statements below
    Duck.quack(Duck)
    Duck.quack(Duck())
    Duck.quack(donald)

if __name__ == '__main__': main()