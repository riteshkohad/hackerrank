from heapq import *


class MedianOfStream:
  def __init__(self):
    # 1. Declare two lists, small is max heap and large is min heap
    self.small, self.large = [], []
    
  # This function should take a number and store it
  def insert_num(self, num):
    # 2. push new element in th max heal (small)
    heappush(self.small, (-1 * num))

    # 2.1 check if lists are not empty and the top element of small is greater then top element of large
    # then pop from small heap and add it in large heap 
    if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
        val = heappop(self.small) * -1
        heappush(self.large, val)

    # 2.2 check the len if small has more items than large + 1
    # then pop from small and push it in large
    # because both lists has to be balanced, max there can be a difference of 1 element
    if len(self.small) > len(self.large) + 1:
        val = heappop(self.small) * -1
        heappush(self.large, val)

    # 2.3 check the len if large has more items than small + 1
    # then pop from large and push it in small
    # because both lists has to be balanced, max there can be a difference of 1 element
    if len(self.large) > len(self.small) + 1:
        val = heappop(self.large)
        heappush(self.small, val * -1)

  # This function should return the median of the stored numbers
  def find_median(self):
    # 3.1 if small and large lists are not empty and are of the same length
    # take a top element from each list and average it
    if self.small and self.large and len(self.small) == len(self.large):
        return (self.small[0] * -1 + self.large[0]) / 2
    
    # 3.2 if length of small list is > then length of large list 
    # then return the top element from small list
    if len(self.small) > len(self.large):
        return self.small[0] * -1
    
    # 3.3 if length of large list is > then length of small list 
    # then return the top element from large list
    if len(self.large) > len(self.small):
        return self.large[0]


# Time complexity analysis:
# Inserting a number: O(log n) due to heappush and heappop operations.
# Finding the median: O(1) as it involves accessing the top elements of the heaps.
# The built-in Python functions like heappush, heappop, and list indexing have a time complexity of O(log n) and O(1) respectively.


# The space complexity of the MedianOfStream class using the Two Heaps pattern is O(n), where n is the number of elements stored in the two heaps (small and large). The space complexity of the heapq module functions used (heappush and heappop) is O(log n) for each operation.




if __name__ == "__main__":
    md = MedianOfStream()
    md.insert_num(22)
    ret = md.find_median()
    print(ret)

    md.insert_num(35)
    md.insert_num(36)

    ret = md.find_median()
    print(ret)

    md.insert_num(27)

    ret = md.find_median()
    print(ret)

