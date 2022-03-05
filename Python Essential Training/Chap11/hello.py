# print('Hello, World.'.upper()) ## can call methods with a literal string
# print('Hello, World.'.swapcase())

# print("""
#     Hello, 
#     World. 
    
#     {}

#     """.format(42 * 7))

# class MyString(str):
#     def __str__(self):
#         return self[::-1]

# s = MyString('Hello, World.')
# print(s)


# s1 = 'Hello, World.'
# s2 = 'this is another string'

# s3 = 'this string' ' that string' # concatenate literal string

# print(s1 + ' ' + s2)
# print(s3)


# x = 42 * 747 * 1000
x = 42
# print('the number is {:,}'.format(x).replace(',', '.'))
# print('the number is {:3f}'.format(x))
# print('the number is {:b}'.format(x))
print(f'the number is {x:.3f}')