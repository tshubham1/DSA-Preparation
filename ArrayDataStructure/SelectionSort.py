# Time Complexity : O(n^2)
# Method implementation
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap happen after every pass
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Driver code
arr = [70, 56, 23, 19, 25, 37, 48]
result = selectionSort(arr)
print(f"Sorted array after applying selection sort is : {result}")