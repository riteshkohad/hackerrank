import heapq


def find_sets(intervals):
    # 1. Sort the given input intervals with respect to their start time
    intervals.sort(key= lambda x: x[0])
    
    # 2. Initialize the min heap and push the end time of the first element onto it
    free_rooms = []     # initialized the heap
    end_time = intervals[0][1]      # take the end time of the first interval 
    heapq.heappush(free_rooms, end_time)        # push it onto the heap 

    # 3. Loop over the remaining elements
    for i in intervals[1:]:
        # 4. In each iteration, compare the start time of each interval with all the end time present in the
        #    heap
        start, end = i      # unpack the interval i in start and end 
        # 5. If the earliest end time of all intervals seen so far (the root of the heat) occurs before the start time 
        #       of the current interval, remove the earliest interval from the heap and push the current interval onto 
        #       the heap
        if free_rooms[0] <= start:          # check the root element with start time 
            heapq.heappop(free_rooms)       # if start is less then pop the root element 
        
        # 6. Allot a new room (add new end time to the heap)
        heapq.heappush(free_rooms, end)
          
    # After processing all the intervals, the size of the heap is the count of meeting rooms needed to hold the meeting 
    return len(free_rooms)
    



if __name__ == "__main__":
    inpt = [[1,3],[2,6],[8,10],[9,15],[12,14]]
    result = find_sets(inpt)
    print(result)