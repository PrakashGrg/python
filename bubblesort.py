def bubblesort(arr):
    # Loop through the entire list
    for i in range(len(arr)):
        # Go through the list up to the unsorted part
        for j in range(len(arr) - i - 1):
            # If the current item is bigger than the next one, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubblesort(numbers)
print("Sorted array is:", sorted_numbers)