from collections import Counter
import heapq


def reorganize_string(str):
    freq = Counter(str)
    
    max_heap = []

    for key in freq :
        heapq.heappush( max_heap, (freq[key] * -1, key))
    
    result = ""

    lst = None
    while max_heap or lst:
        if lst and not max_heap:
            return ""

        val, car = heapq.heappop(max_heap)
        
        result += car
        val += 1

        if lst:
            heapq.heappush(max_heap, lst)
            lst = None

        if val != 0:
            lst = (val, car)

    return result


if __name__ == "__main__":
    inpt = "aaaaabbbbbbb"
    result = reorganize_string(inpt)
    print(result)