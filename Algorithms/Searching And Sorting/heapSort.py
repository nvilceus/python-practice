# O(nlog(n)) time complexity
# O(1) space complexity

def heapify(arr, n, i):
    largest = i # initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]: # see if left child of root exists and is greater than root
        largest = l
    if r < n and arr[largest] < arr[r]: # see if right child of root exists and is greater than root
        largest = r
    if largest != i: # change root if needed
        arr[i], arr[largest] = arr[largest], arr[i] # swap
        heapify(arr, n, largest) # heapify the root

def heapSort(arr): # the main function to sort an array of given size
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1): # build max heap
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1): # one by one extract elements
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

def main():
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr)
    print('Sorted Array: {}'.format(arr))

if __name__ == '__main__': main()