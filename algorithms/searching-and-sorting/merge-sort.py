# O(nlog(n)) time complexity
# O(n) space complexity

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # finding the mid of the array
        L = arr[:mid] # dividing the array elements into left half
        R = arr[mid:] # dividing the array elements into right half
        mergeSort(L) # sorting the left half
        mergeSort(R) # sorting the right half
        i = j = k = 0
        while i < len(L) and j < len(R): # copy data to temp arrays L[] and R[]
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L): # checking if any element was left
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R): # checking if any element was left
            arr[k] = R[j]
            j += 1
            k += 1       

def main():
    arr = [12, 11, 13, 5, 6, 7]
    mergeSort(arr)
    print('Sorted Array: {}'.format(arr))

if __name__ == '__main__': main()