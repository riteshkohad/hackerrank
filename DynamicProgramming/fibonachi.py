# Using simple recurrestion 
def fib (x):
    if x <= 2:
        return 1
    
    return fib(x-1) + fib(x-2)

# Using dynamic programming 
def fib_dp (x, memo):
    if x in memo:
        return memo[x]
    
    if x <= 2:
        return 1
    
    res = fib_dp(x-1, memo) + fib_dp(x-2, memo)
    memo[x] = res
    return res


# Using dynamic programming optional parameter 
def fib_dpx (x, memo_op = {}):
    if x in memo_op:
        return memo_op[x]
    
    if x <= 2:
        return 1
    
    res = fib_dpx(x-1, memo_op) + fib_dpx(x-2, memo_op)
    memo_op[x] = res
    return res



if __name__ == "__main__":
    print(fib(5))

    dic = {}
    print(fib_dp(500,dic))

    print(fib_dpx(500))

