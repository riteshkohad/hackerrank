import heapq
from interval import Interval


"""
Time complexity: The time complexity of the function Employee Free Time is O(n log n), where n is the total number of intervals across 
all employees. This is because the function iterates through each interval in the schedule and adds it to a heap, which takes O(n log n) 
time. Then, it pops intervals from the heap until it is empty, which also takes O(n log n) time. Therefore, the overall time complexity 
is O(n log n).

Space complexity: The space complexity of the function Employee Free Time is O(n), where n is the total number of intervals in the schedule. 
This is because we are storing all the intervals in a heap, which requires O(n) space. Additionally, we are creating a list called output 
to store the merged intervals, which also requires O(n) space in the worst case.
"""



def employee_free_time(schedule):
    heap = []
    for i in schedule:
        for j in i:
            heap.append([j.start, j.end])

    heapq.heapify(heap)

    pst, ped = st, ed = heapq.heappop(heap)
    output = []
    while heap:
        st, ed = heapq.heappop(heap)
        # print(f"{st}:{ed}")
        if st > ped:
            output.append(Interval(ped, st))

        pst = st
        ped = max(ped, ed)
        
    return output


def main():
    inpt = [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]]
    ret_val = employee_free_time(inpt)
    print(ret_val)


if __name__ == "__main__":
    main()