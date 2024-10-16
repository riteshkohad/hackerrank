
# unfinished one

def max_value(n, index, max_sum):
    result = []
    ms = max_sum

    val, last_val = 0, 1
    for i in range(1, n+1):
        val = min( round(ms // ((n+1)-i)), i)
        val = min(val, last_val + 1 )
        ms = ms - val
        
        result.append(val)
        last_val = val

    return result


if __name__ == "__main__":
    inpt = 5
    i = 3
    ms = 15
    result = max_value(inpt, i, ms)
    print(result)