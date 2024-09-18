
def merge_intervals(intervals):
    # variable to output values
    output = []
    # take a first element and find start and end of the first interval 
    start, end = intervals[0][0], intervals[0][1]
    # insert it in the output array
    output.append([start, end])

    # start loop from 1 element, 0th one is already in the output array
    for i in range(1, len(intervals)):
        # check the last end is >= current start
        if (end >= intervals[i][0]):
            # if so, take a max of current end and last end 
            end = max(end, intervals[i][1])
            # update the output array's last element's (-1) end 
            output[-1][1] = end
        else:
            # otherwise, set the new start and end 
            start, end = intervals[i][0], intervals[i][1]
            # add it in the output 
            output.append([start, end])
    # return the output
    return output


if __name__ == "__main__":
    inpt = [[1,9],[3,8],[4,4]]
    output = merge_intervals(inpt)
    print(output)