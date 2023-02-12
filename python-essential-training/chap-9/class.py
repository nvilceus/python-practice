class Duck:
    ## Data ##
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'
    ## Methods ##
    def quack(self): # first parameter of a method is always self which is a reference to the object and not the class
        print(self.sound) # dot operator dereferences the object

    def move(self):
        print(self.movement)

def main():
    donald = Duck() # donald is an object instantiated from the class Duck
    donald.quack() # dot operator dereferences the object donald to get to the method quack 
    donald.move()

if __name__ == '__main__': main()