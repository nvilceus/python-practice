class Animal:
    def __init__(self, **kwargs): # __init__ operates as a constructor
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten' # does not exist in the class without having been constructed into an object
        self._name = kwargs['name'] if 'type' in kwargs else 'fluffy' # users are discouraged from accessing these variables directly
        self._sound = kwargs['sound'] if 'type' in kwargs else 'rawr' 

    def type(self): # accessor returns the value of the object variables
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name= 'donald', sound='quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal())

if __name__ == '__main__': main()