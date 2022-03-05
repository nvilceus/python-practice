# O(log(n)) time complexity
# O(log(n)) space complexity

# Recursive
def binarySearch(arr, l, r, x):
    if r >= l: # check base case
        mid = l + (r - l) // 2
        if arr[mid] == x: # if element is present at the middle return itself
            return mid
        elif arr[mid] > x: # if element is smaller than mid, then it can only be present in left subarray
            return binarySearch(arr, l, mid - 1, x)
        else: # else the element can only be present in right subarray
            return binarySearch(arr, mid + 1, r, x )
    else: # element is not present in the array
        return -1

# O(log(n)) time compexity
# O(1) space complexity

# Iterative
# def binarySearch(arr, l, r, x):
#     while 1 <= r: # check base case
#         mid = 1 + (r - l) // 2
#         if arr[mid] == x: # if element is present at the middle return itself
#             return mid
#         elif arr[mid] < x: if element is greater than mid, then it can only be present in right subarray
#             l = mid + 1
#         else: if element is smaller than mid, then it can only be present in left subarray
#             r = mid - 1
#     return -1 # element is not present in the array

def main():
    arr = [2, 3, 4, 10, 40]
    x = 10
    r = len(arr) - 1
    l = 0
    result = binarySearch(arr, l, r, x)
    if (result == -1):
        print('Element is not present in array') 
    else:
        print('Element is present at index {}'.format(result))

if __name__ == '__main__': main()