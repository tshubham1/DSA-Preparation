# Binary Search Algorithm using recursion
# Time complexity : O(log n)
# Method implementation
def binarySearch(arr, x, left, right):
    

    while left <= right:

    # lower bound while division
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            # right side of the mid
            # search space --> mid + 1 to right
            return binarySearch(arr, x, mid + 1, right)
        
        else:
            # left side of the mid
            # search space --> left to mid - 1
            return binarySearch(arr, x, left, mid - 1)
    # searching element is not present in an array 
    return -1
        
# driver code
# sorted array
arr = [20, 30, 40, 50, 60, 70, 80, 90]
#  x - element to be searched in array
x = 80
# starting index
left = 0
# last index
right = len(arr) - 1
result = binarySearch(arr, x, left, right)
print(f"The element is present at: {result}")