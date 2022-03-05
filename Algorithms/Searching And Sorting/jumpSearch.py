# O(sqrt(n)) time complexity
# O(1) space complexity

import math

def jumpSearch(arr, x, n):
    step = math.sqrt(n) # finding block size to be jumped
    prev = 0 # finding the block where element is present (if it is present)
    while arr[int(min(step, n) - 1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    while arr[int(prev)] < x: # doing a linear search for x in block beginning with prev
        prev += 1
        if prev == min(step, n): # if we reached next block or end of array, element is not present
            return -1
    if arr[int(prev)] == x: # if element is found
        return prev
    return -1

def main():
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
        34, 55, 89, 144, 233, 377, 610]
    x = 55
    n = len(arr)
    index = jumpSearch(arr, x, n)
    print('Number {a} is at index {b:.0f}'.format(a = x, b = index))

if __name__ =='__main__': main()