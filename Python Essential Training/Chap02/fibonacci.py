# Simple fibonacci series
# The sum of two elements defines the next set

a, b = 0,1
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print() # Line ending