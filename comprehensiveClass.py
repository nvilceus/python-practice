class names:
    def __init__(self, args): # constructor
        self.args = args
    
    def addName(self, newName):
        self.args.append(newName)
        return self.args

    @classmethod
    def firstNames(cls, args):
        first_names = []
        for i in range(len(args)):
            f,l = args[i].split(' ')
            first_names.append(f)
        return cls(first_names)
    @classmethod
    def lastNames(cls, args):
        last_names = []
        for i in range(len(args)):
            f, l = args[i].split(' ')
            last_names.append(l)
        return cls(last_names)
    @staticmethod
    def deleteLastIndex(args):
        del args[-1]
        return args

def main():
    args1 = ('John Collins', 'Noah Vilceus', 'Spencer Stevens', 'Tom Ford', 'Loretta Scott')
    args2 = ('Tony Lemons', 'Phillip Pots', 'Sarah Baker', 'Alvin Aldridge', 'Nate Diggs')
    x = names.firstNames(list(args1))
    y = names.lastNames(list(args2))
    print(f'List 1 args are: {x.args}')
    print(f'List 2 args are: {y.args}')
    print(f'List 1 args are now: {x.deleteLastIndex(x.args)}')
    x.addName(names.firstNames(list(args1)).args[len(args1)-1]) # adds 'Loretta'to the end of List 1
    print(f'List 1 args are now: {x.args}')
    z = names(list(args1))
    print(f'List 3 args are: {z.args}')
    z.addName('Sam Smith')
    w = names.firstNames(z.args) # @classmethod does not have direct access to instance object variable so creates a new list object, w
    print(f'List 4 args are: {w.args}')
    print(f'List 3 args are now: {z.args}') # returns list(args1) with 'Sam Smith' appended
    print(f'Original args1 is: {list(args1)}')

if __name__ == '__main__': main()