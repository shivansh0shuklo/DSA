#The Challenge: You are given an array prices. 
# For each item i, you get a discount equal to the price of 
# the first item to its right whose price is less than 
# or equal to prices[i]. If no such discount exists, 
# you pay the full pric 
# can you exaplin in a more detail howw to approach this
def nearest_smaller_to_right(prices):
    stack = []
    result = [0]*len(prices)
    for i in range(len(prices)-1,-1,-1):
        # discount = 0
        while (len(stack)>0 and stack[-1]>prices[i]):
            stack.pop()
        if(len(stack)==0):
            discount = 0
        elif(len(stack)>0 and prices[i]>stack[-1]):
            discount = stack[-1]
        result[i] = prices[i]-discount
        stack.append(prices[i])
    return result
print(nearest_smaller_to_right([8, 4, 6, 2, 3]))