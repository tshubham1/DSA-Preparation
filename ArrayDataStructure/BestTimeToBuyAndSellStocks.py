
# Time complexity : O(n)

# Function definition
def findmaxProfit(price):
    # initialization
    # minPrice would be higher at this point
    minPrice = float('inf')
    # maxProfit will be lower at this point
    maxProfit = 0

    for i in range(len(price)):
        if price[i] < minPrice:
            minPrice = price[i]

        elif price[i] - minPrice > maxProfit:
            maxProfit = price[i] - minPrice
    
    return maxProfit

# Driver code
price = [7, 1, 5, 3, 6, 8]
maxProfit_value = findmaxProfit(price)
print("The maximum profit of buying and selling the stocks is : ", maxProfit_value)