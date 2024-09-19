from interval import Interval

# this is another easier way of solving this problem
# first way was to use heapq, see first code 

def employee_free_time(schedule):
    # define a list for storing all the schedules
    schedule_list = []

    # Iterate thru all the employees
    for s in schedule:
        # iterate thru all the schedules for each employee 
        for i in s:
            # add schedule to the list 
            schedule_list.append([i.start, i.end])
    
    # sort a list by schedule start time (0th index)
    schedule_list = sorted(schedule_list, key=lambda x: x[0])
    # print(schedule_list)
    # define a variable for start and stop of the first schedule 
    p_start, p_end = schedule_list[0]

    # define variable for result 
    output = []
    # go over each schedule from schedule list
    for item in range(1, len(schedule_list)) :
        # take start and end time of each schedule
        start, end = schedule_list[item]
        # compare the start time of each schedule with the previous schedule 
        if start <= p_end:
            # if current start time is smaller than the previous end that means it can be merged 
            # take max of previous and current end time
            p_end = max(end, p_end)
            # take min of previous and current end time
            p_start = min(start, p_start)
        else:
            # if not that means there is a gap, that gap is what asked for so add it in the output 
            # gap is from the previous end till current start time
            output.append([p_end, start])
            # make current time as previous to compare with next schedule 
            p_start, p_end = schedule_list[item]

    # return the output at the end
    return output

        



if __name__ == "__main__":
    inpt = [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]]
    ret_val = employee_free_time(inpt)
    print(ret_val)
