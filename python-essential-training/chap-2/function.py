def function(n = 1):
    print(n)
    return n * 2 # Returns n * 2 for print(x) statement instead of None

function(47)
x = function(42) # Returns a default value of None (abscense of a value special to Python)
print(x)