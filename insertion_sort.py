# Function to perform insertion sort
def insertion_sort(arr):
    # Traverse from 1 to len(arr)-1
    for i in range(1, len(arr)):
        key = arr[i]

        # Move the elements of arr[0...i-1] that are greater than
        # the key to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    insertion_sort(array)
    print("Sorted Array Is: " + str(array))
