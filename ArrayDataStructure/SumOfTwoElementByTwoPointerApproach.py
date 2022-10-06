# Two pointer approach
# Time complexity : O(n) -- optimized approach

# Note: If you solve same with linear search -- two for loops --> O(n^2)
#       Binary search -- Time complexity --> O(nlogn)

# O(n^2) < O(nlogn) < O(n)

# Function implementation
def addTwoValues(arr, sum_value, left, right):

    while left <= right:

        if arr[left] + arr[right] == sum_value:
            return arr[left], arr[right]
        
        elif arr[left] + arr[right] > sum_value:
            right = right - 1
        
        else:
            left = left + 1
    
    return -1


# Driver code
arr = [20, 40, 60, 80, 90, 120, 240]
sum_value = 210
left = 0
right = len(arr) - 1
result = addTwoValues(arr, sum_value, left, right)
print(result)