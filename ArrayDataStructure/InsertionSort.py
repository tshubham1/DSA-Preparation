# Time complexity : O(n^2)
# Method implementation
def insertionSort(arr):

    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j -1
    
        arr[j+1] = key
    return arr

# Driver code
arr = [75, 90, 100, 95, 85, 80]
result = insertionSort(arr)
print("Array after applying the insertion sort: ", result)