# O(n) time complexity
# O(1) space complexity

def search(arr, x):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1

def main():
    arr = [2, 3, 4, 1, 40]
    x = 10
    result = search(arr, x)
    if result == -1:
        print('Element is not present in array') 
    else:
        print('Element is present at index {}'.format(result))

if __name__ == '__main__': main()