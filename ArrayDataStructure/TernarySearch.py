
# Time complexity : O(logn)
# Function implementation
def ternarySearch(arr, i, j, key):

    while i <= j:
        # Computing the values of mid1 and mid2
        # from left
        mid1 = i + (j - i)//3
        # from right
        mid2 = j - (j - i)//3

        if arr[mid1] == key:
            return mid1
        
        elif arr[mid2] == key:
            return mid2
        
        elif key < arr[mid1]:
            return ternarySearch(arr, i, mid1-1, key)

        elif key > arr[mid2]:
            return ternarySearch(arr, mid2+1, j, key)
        else:
            return ternarySearch(arr, mid1+1, mid2-1, key)

    return -1


# Driver code 
arr = [20, 25, 47, 56, 59, 63, 65, 79, 82]
i = 0
j = len(arr) - 1
key = 47
# Function calling
result = ternarySearch(arr,i, j, key)
print(result)