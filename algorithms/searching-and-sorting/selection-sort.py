# O(n^2) time complexity
# O(1) space complexity

def selectionSort(arr):
    for i in range(len(arr)): # traverse through all array elements
        min_idx = i #find the minimum element in remaining unsorted array
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # swap the found minimum element with the first element
    return arr

def main():
    arr = [64, 25, 12, 22, 11]
    selectionSort(arr)
    print('Sorted Array: {}'.format(arr))

if __name__ == '__main__': main()