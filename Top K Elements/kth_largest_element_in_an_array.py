from heapq import heappop, heappush


def find_kth_largest(nums, k):
    # 1. define a min heap as we are looking for a largest kth element (max heap if it was smallest)
    min_heap = []

    # push first k elements in the min heap
    for i in range(k):
        heappush(min_heap, nums[i])
    
    # for rest of the element, check if root of the heap is smaller than the current element then pop it and push the new one
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])

    # return the root element from he min heap
    return min_heap[0]


if __name__ == "__main__":
    inpt = [10,-5,0,-8,4]
    k = 2
    result = find_kth_largest(inpt, k)
    print(result)