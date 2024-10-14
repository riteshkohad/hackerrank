from heapq import heappush, heappop
from collections import Counter

def top_k_frequent(arr, k):
    # 1. create a hashmap of the input array by its frequency and define min heap
    counts = Counter(arr)
    min_heap = []

    # 2. iterate thru all the items of the hash map and push it in the min heap by its frequency 
    for key, val in counts.items():
        tpl = (val, key)
        heappush(min_heap, tpl)

    # 3. pop all the elements > K
    while len(min_heap) > k:
        heappop(min_heap)

    # 4. define result list and pop all the remaining elements from heap to return 
    result = []
    while min_heap:
        result.append(heappop(min_heap)[1])
    
    return result


if __name__ == "__main__":
    inpt = [1, 1, 2, 4, 5, 5]
    k = 2
    result = top_k_frequent(inpt, k)
    print(result)