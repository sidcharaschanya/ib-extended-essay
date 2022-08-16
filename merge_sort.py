# Function to perform merge sort
def merge_sort(arr):
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2

        # Dividing the array elements into two halves
        left = arr[:mid]
        right = arr[mid:]

        # Sorting the first half
        merge_sort(left)

        # Sorting the second half
        merge_sort(right)

        i = j = k = 0

        # Merge the temporary arrays left[] and right[] back into arr[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any elements remained in left[] and right[]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    merge_sort(array)
    print("Sorted Array Is: " + str(array))
