
"""
Time complexity:
The time complexity of the function is O(n), where n is the length of the prices list. This is because the function uses a 
sliding window approach to iterate through the prices list once, comparing each price with the previous one. The max function 
has a time complexity of O(1) as it operates on a constant number of elements.

Space complexity:
The space complexity of the function is O(1) because it only uses a constant amount of extra space to store the variables buy, 
sell, max_profit, and profit. The space complexity of the built-in Python function max() is also O(1) because it only returns 
the maximum value among the given arguments without using any additional space.
"""


def max_profit(prices):
    buy, sell = 0, 1
    max_profit = 0 

    while sell < len(prices):
        profit = (prices[sell] - prices[buy])
        if prices[buy] < prices[sell]:
            max_profit = max(profit, max_profit)
        else:
            buy = sell
        
        sell += 1

    return max_profit


if __name__ == "__main__":
    inpt = [1,2,4,2,5,7,2,4,9,0,9]
    ret_val = max_profit(inpt)
    print(ret_val)

