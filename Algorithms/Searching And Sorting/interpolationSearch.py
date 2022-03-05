# O(log(log(n))) --> O(n) average to worst case time complexity
# O(1) space complexity

def interpolationSearch(arr, lo, hi, x):
    if arr[lo] <= arr[hi] and x >= arr[lo] and x <= arr[hi]: # since array is sorted, an element present in array must be in range defined by corner
        mid = lo + (x - arr[lo]) * (hi - lo) // (arr[hi] - arr[lo]) # probing the position with keeping uniform distribution in mind
        if arr[mid] == x: # condition target found
            return mid
        elif arr[mid] < x: # if x is larger, x is in right subarray
            return interpolationSearch(arr, mid + 1, hi, x)
        else: # if x is smaller, x is in left subarray
            return interpolationSearch(arr, lo, mid - 1, x) 
    return -1 # if x is not in array

def main():
    arr = [10, 12, 13, 16, 18, 19, 20, 
        21, 22, 23, 24, 33, 35, 42, 47]
    x = 10
    n = len(arr)
    lo = 0
    hi = n - 1
    index = interpolationSearch(arr, lo, hi, x)
    if index != -1:
        print('Element found at index {}'.format(index))
    else:
        print('Element not found')

if __name__ == '__main__': main()