def main():
    animals = dict(kitten = 'meow', puppy = 'ruff!', lion = 'grrr', 
        giraffe = 'I am a giraffe!', dragon = 'rawr')
    # animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr', # Creates a dictionary without using dict()
    #     'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}
    # for k, v in animals.items():
    #     print(f'{k}: {v}')
    # for k in animals.keys(): print(k) # Prints list of the keys
    # for v in animals.values(): print(v) # Prints list of the values
    # print(animals['lion']) # A dictionary is indexed by its keys
    # animals['lion'] = 'I am a lion'
    # animals['monkey'] = 'haha'
    # print('lion' in animals) # Searches for a key and returns a boolean
    # print('found!' if 'godzilla' in animals else 'nope!') # Prints a conditional expression
    print(animals.get('godzilla')) # Returns a value of None if you don't want the KeyError exception
    print_dict(animals)

def print_dict(o):
    for k, v in o.items():
        print(f'{k}: {v}')
    # for x in o: print(f'{x}: {o[x]}')

if __name__ == '__main__': main()