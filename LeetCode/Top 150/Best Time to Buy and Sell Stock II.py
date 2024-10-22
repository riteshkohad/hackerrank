

def maxProfit(prices) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0
    for i in range(len(prices)):
        # print(prices[i])
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            if i < len(prices) - 1:
                if prices[i + 1] != None and prices[i] > prices[i + 1]:
                    max_profit += prices[i] - min_price 
                    min_price = prices[i]
            else:
                max_profit += prices[i] - min_price 

    return max_profit


if __name__ == "__main__":
    inpt = [7,6,4,3,1]
    result = maxProfit(inpt)
    print(result)
