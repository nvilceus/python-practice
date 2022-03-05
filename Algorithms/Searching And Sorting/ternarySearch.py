# O(log3(n)) time complexity # worst case takes more comparisons than binary search
# O(1) space complexity

def ternarySearch(arr, l, r, x):
    if r >= l:
        mid1 = l + (r - l) // 3
        mid2 = mid1 + (r - l) // 3
        if arr[mid1] == x: # if x is present at the mid1
            return mid1
        if arr[mid2] == x: # if x is present at the mid2
            return mid2
        if arr[mid1] > x: # if present in left one-third
            return ternarySearch(arr, l, mid1 - 1, x)
        if arr[mid2] < x: # if present in reight one-third
            return ternarySearch(arr, mid2 + 1, r, x)
        return ternarySearch(arr, mid1 + 1, mid2 - 1, x) # if present in middle one-third
    return -1 # we reac here when element is not present in array

def main():
    arr = [2, 3, 4, 10, 40]
    x = 10
    r = len(arr) - 1
    l = 0
    result = ternarySearch(arr, l, r, x)
    if result == -1:
        print('Element is not present in array') 
    else:
        print('Element is present at index {}'.format(result))

if __name__ == '__main__': main()