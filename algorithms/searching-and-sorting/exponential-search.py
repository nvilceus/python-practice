# O(log(n)) time complexity
# O(1) space complexity

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x )
    else:
        return -1

def exponentialSearch(arr, n, x):
    if arr[0] == x: # if x is present at first location itself
        return 0
    i = 1 # find range for binary search j by repeated doubling
    while i < n and arr[i] <= x:
        i = i * 2
    return binarySearch(arr, i // 2, min(i, n - 1), x) # call binary search for the found range

def main():
    arr = [2, 3, 4, 10, 40]
    n = len(arr)
    x = 2
    result = exponentialSearch(arr, n, x)
    if result == -1:
        print('Element is not present in array') 
    else:
        print('Element is present at index {}'.format(result))

if __name__ == '__main__': main()