class Animal:
        #   x = [1, 2, 3] ## class vairable and not object variable because defined in class and not in a method (not encapsulated)
        def __init__(self, **kwargs): 
            self._type = kwargs['type'] if 'type' in kwargs else 'kitten' 
            self._name = kwargs['name'] if 'type' in kwargs else 'fluffy' # no private variables in Python so underscore means do not touch this
            self._sound = kwargs['sound'] if 'type' in kwargs else 'meow' 

        def type(self, t = None): # method to set and get the object variable type
            if t: self._type = t
            return self._type 

        def name(self, n = None):
            if n: self._name = n
            return self._name

        def sound(self, s = None):
            if s: self._sound = s
            return self._sound

        def __str__(self): 
            return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name= 'donald', sound='quack')
    a0.sound('bark')
    print(a0)
    print(a1)

    # print(a0.x)
    # a1.x[0] = 7
    # print(a0.x)

if __name__ == '__main__': main()