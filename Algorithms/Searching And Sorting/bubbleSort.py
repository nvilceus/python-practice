# O(n^2) time complexity
# O(1) space complexity

def bubbleSort(arr):
    n = len(arr)
    for i in range(n): 
        for j in range(0, n - i - 1): # traverse the array from 0 to n-i-1
            if arr[j] > arr[j + 1]: # swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(arr)
    print('Sorted Array: {}'.format(arr))

if __name__ == '__main__': main()