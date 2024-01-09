import heapq


"""
Time complexity: The time complexity of the function Meeting Rooms II is O(n log n), where n is the number of intervals. 
This is because the function first sorts the intervals using the built-in sorted() function, which has a time complexity 
of O(n log n). Then, it iterates through the sorted intervals and performs operations using the heapq module, which has a 
time complexity of O(log n) for push and pop operations. Therefore, the overall time complexity is dominated by the sorting 
step, resulting in O(n log n).

Space complexity: The space complexity of the function Meeting Rooms II is O(n), where n is the number of intervals. This is because 
we are using a heap data structure to store the end times of the meetings. The size of the heap will be at most the number of intervals, 
so the space complexity is linear with respect to the number of intervals. Additionally, the space complexity of the built-in Python 
functions used in the code (such as sorted() and heapq.heappush()) is also O(n) in the worst case.
"""

def find_sets(intervals):

    intervals = sorted(intervals, key= lambda z: z[0])
    heap = []

    # add first end time of the meeting into the heap 
    heapq.heappush(heap, intervals[0][1])
    
    # iterate thru all the interval except 1 
    for i in intervals[1:]:
        # take a earliest element from queue 
        earliestEndTime = heapq.heappop(heap)
        
        # take current time 
        currentStartTime = i[0]

        # check if current time is greater than closing time 
        if currentStartTime >= earliestEndTime:
            # if so then replace the current end time with earliest time 
            earliestEndTime = i[1]
        else:
            # if not, add new element to the heap 
            heapq.heappush(heap, i[1])
            
        # add the earliest time back to the heap with updated time 
        heapq.heappush(heap, earliestEndTime)   
        

    # now we should have all the rooms we need
    rooms = len(heap)

    return rooms



def main():
    inpt = [[2,8],[3,4],[3,9],[5,11],[8,20],[11,15]]
    ret_val = find_sets(inpt)
    print(ret_val)


if __name__ == "__main__":
    main()