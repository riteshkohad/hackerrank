

def maxProfit(prices) -> int:
    min_price = prices[0]
    max_profit = 0

    for i in prices:
        if i < min_price:
            min_price = i
        else:
            max_profit =  max(max_profit, i - min_price)
    
    return max_profit

if __name__ == "__main__":
    inpt = [7,6,4,3,1]
    result = maxProfit(inpt)
    print(result)
