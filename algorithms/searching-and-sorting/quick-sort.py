# O() time complexity
# O() space complexity

def partition(start, end, arr):
    pivotIndex = start # initializing pivot's index to start
    pivot = arr[pivotIndex]
    while start < end: # this loop runs till start pointer crosses end pointer, an when it does we swap the pivot with element on end pointer
        while start < len(arr) and arr[start] <= pivot: # increment the start pointer till it finds an element greater than pivot
            start += 1
        while arr[end] > pivot: # decrement the end pointer till it finds an element less than pivot
            end -= 1
        if start < end: # if start and end have not crossed wach other, swap the numbers on start and end
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivotIndex] = arr[pivotIndex], arr[end] # swap pivot element on end pointer. This puts pivot in its correct sorted place
    return end # returning end pointer do divide the array into 2

def quickSort(start, end, arr):
    if start < end:
        p = partition(start, end, arr) # p is partitioning index, arr[p] is at right place
        quickSort(start, p - 1, arr) # sort elements before partition and after partition
        quickSort(p + 1, end, arr)

def main():
    arr = [10, 7, 8, 9, 1, 5]
    quickSort(0, len(arr) - 1, arr)
    print('Sorted Array: {}'.format(arr))

if __name__ == '__main__': main()