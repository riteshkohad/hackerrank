
def insert_interval(existing_intervals, new_interval):
    # variable for result
    output = []
    # variables to loop 
    i, n = 0, len(existing_intervals)

    # loop thru all existing intervals where start is less than new interval's start
    # and insert all those in the output array
    while i < n and existing_intervals[i][0] < new_interval[0]:
        output.append(existing_intervals[i])
        i += 1
    
    # now that all the elements less than the new interval's start date is in the output
    # take new interval and check if start is less than the last output's end if so then merge those two
    if len(output) > 0 and new_interval[0] <= output[-1][1]:
        # merge the end, take the max of new end or last output's end
        output[-1][1] = max(output[-1][1], new_interval[1])
    else:
        # if not, that means new interval is independent
        # so insert it in the output array 
        output.append(new_interval)
    
    # now that we took care of the new interval, loop thu the entire array
    # and merge as needed
    while i < n:
        # take start and end from existing intervals for the current element 
        stat, end = existing_intervals[i][0], existing_intervals[i][1]

        # check if start is less than the last output's end
        if stat<= output[-1][1]:
            # if so then take a max of current end or last output's end
            end = max(output[-1][1], end)
            # and update the output array with max
            output[-1][1] = end
        else:
            # otherwise, add start and end to the output array 
            output.append([stat, end])
        
        # increment the loop counter 
        i+=1

    # return the output
    return output



if __name__ == "__main__":
    inpt = [[1,4],[5,6],[7,8],[9,10]]
    inpt2 = [1, 5]

    result = insert_interval(inpt, inpt2)
    print(result)