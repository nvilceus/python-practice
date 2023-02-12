class bunny:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return f'repr: the number of bunnies is {self._n}'
    def __str__(self):
        return f'str: the number of bunnies is {self._n}'

x = bunny(47)
print(repr(x)) # repr prints the best possible string representation of an object
print(x)
print(ascii(x)) # escapes any special characters like an emoji
# print(chr(128406)) # prints a character represented by a unicode position and ord() does the opposite