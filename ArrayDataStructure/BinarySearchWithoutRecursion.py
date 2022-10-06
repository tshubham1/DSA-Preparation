# Binary Search Algorithm with iterative approach
# Function definition

def binarySearch(arr, x, left, right):
    

    while left <= right:
        # lower bound while division
        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# driver code
# sorted array
arr = [20, 30, 40, 50, 60, 70, 80, 90]
x = 80
left = 0
right = len(arr) - 1
# function calling
result = binarySearch(arr, x, left, right)
print(f"The element is present at: {result}")