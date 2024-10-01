import heapq

def maximum_capital(c, k, capitals, profits):
    # 1. Define heaps for max_profit and min_capital
    max_profit = []
    # 1.1 load min_capital with tuple of (capitals[i], profits[i] )
    min_capital = [ (cap, p) for cap, p in zip(capitals, profits)]
    # 1.2 heapify min_capital, it will heapify based on the 0th index of tuple 
    heapq.heapify(min_capital)

    # 2. Repeat till k chances 
    for i in range(k):
        # keep popping items as long as min_capital heap giving smaller elements than c
        while min_capital and min_capital[0][0] <= c:
            # 2.1 pop and collect the data after pop
            cap, p = heapq.heappop(min_capital)

            # 2.2 add all popped profits in the max_profit heap
            # to make max heap in python you have to use -ve numbers
            heapq.heappush(max_profit, -1 * p)  # convert into -ve to make heap maxHeap
        
        # 3. after the loop, check if max_profit is empty
        if not max_profit:
            # if yes, then return nothing 
            break
        
        # 4. otherwise, pop the max profit from max_profit max heap and add it to the 
        # initial capital c 
        c += (-1 * heapq.heappop(max_profit))
    # 5. Return 
    return c


if __name__ == "__main__":
    c, k = 3, 1
    capital = [0, 2, 3, 4]
    profit = [7, 3, 5, 2]
    ret_val = maximum_capital(c, k, capital, profit)
    print(ret_val)