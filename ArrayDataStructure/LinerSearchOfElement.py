# Time complexity : O(n)

# Method implementation
def searchOfElement(arr, x):

    for i in range(0, len(arr)):
        if arr[i] == x:
            return i
# If element is not present then return -1 
    return -1


# Driver code 
arr = [10, 20, 40, 60, 30, 47, 88]
# element to search in array
x = 47
result = searchOfElement(arr, x)
print(f"The element is found at: {result}")
