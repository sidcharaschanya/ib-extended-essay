# This function takes the last element as the pivot, places
# the pivot element at its correct position in the sorted
# array, and places all elements smaller than the pivot to
# the left of the pivot and all greater elements to the
# right of the pivot


def partition(arr, start, end):
    # index of the smaller element
    i = start - 1

    # the pivot
    pivot = arr[end]

    for j in range(start, end):
        # If the current element is smaller than the pivot
        if arr[j] < pivot:
            # increment the index of the smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


# Function to perform quicksort
def quicksort(arr, start, end):
    if start < end:
        # pi is the partitioning index, arr[pi] is now at the right place
        pi = partition(arr, start, end)

        # Separately sort the elements before and after the partition
        quicksort(arr, start, pi - 1)
        quicksort(arr, pi + 1, end)


if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    quicksort(array, 0, len(array) - 1)
    print("Sorted Array Is: " + str(array))
