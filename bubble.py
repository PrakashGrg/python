def swap(a, b):
    return b, a


def bubblesort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                swap(arr[j], arr[j+1])
    return arr

bubblesort([64, 34, 25, 12, 22, 11, 90])
print("Sorted array is:", bubblesort([64, 34, 25, 12, 22, 11, 90]))