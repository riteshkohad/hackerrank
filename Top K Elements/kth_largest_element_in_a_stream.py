import heapq

class KthLargest:
    # Constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        # 1. Initialize the min_heap because we need to find kth largest element 
        self._min_heap = []
        self.k = k

        # 2. Push first K elements in the min heap
        for i in range(k):
            heapq.heappush(self._min_heap, nums[i])

        # 2.1 for rest of the elements, call add function which will add an element to the list and return the Kth largest element 
        for i in range(k, len(nums)):
            # heapq.heappush(self._min_heap, nums[i])
            self.add(nums[i])

        # print(self._min_heap)

    # Adds element in the heap and return the Kth largest
    def add(self, val):
        # 3. Check the length of the heap, if it is less than the K, push the value 
        if len(self._min_heap) < self.k:
            heapq.heappush(self._min_heap, val)
        else:
            # Otherwise check if value is greater than the root of the min_heap, if so, then pop the element from heap and push the value 
            if self._min_heap[0] < val:
                heapq.heappop(self._min_heap)
                heapq.heappush(self._min_heap, val)

        # 4. return the root element of the min_heap
        return self._min_heap[0]

if __name__ == "__main__":
    inpt = [4,5,8,2]
    k = 3

    kl = KthLargest(k, inpt)

    result = kl.add(3)
    print(result)
    result = kl.add(5)
    print(result)
    result = kl.add(10)
    print(result)
    result = kl.add(9)
    print(result)
    result = kl.add(4)
    print(result)
    # [[3,],[3],[5],[10],[9],[4]]
