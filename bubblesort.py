def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def bubblesort(arr):
    n = len(arr)
        # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
    return arr

print("Sorted array is:", bubblesort([64, 34, 25, 12, 22, 11, 90]))