# O(n^2) time complexity
# O(1) space complexity

def insertionSort(arr):
    for i in range(1, len(arr)): # traverse through 1 to len(arr)
        key = arr[i]
        j = i - 1 # move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key

def main():
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    print('Sorted Array: {}'.format(arr))

if __name__ == '__main__': main()