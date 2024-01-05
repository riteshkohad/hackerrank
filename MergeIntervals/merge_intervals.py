
"""
Time complexity:
The time complexity of the function Merge Intervals is O(n), where n is the number of intervals in the input array. This is 
because we iterate through each interval once in the for loop. The built-in Python functions used in the code, such as indexing, 
appending, and max, have constant time complexity and do not affect the overall time complexity of the function.

Space complexity:
The space complexity of the function Merge Intervals is O(n), where n is the number of intervals in the input array. This is because 
the output array will have at most n elements, and the additional space used by the function is constant. The built-in Python functions 
invoked by the code, such as max(), do not significantly impact the overall space complexity.
"""

def merge_intervals(intervals):
    # take the first element in given array and add it in the output array
    output = [intervals[0]]

    # loop thru all the input element starting from 2nd element 
    for start, end in intervals[1:]:
        # take a last element of the output array 
        last_output_element = output[-1]
        # take a 2nd element which is the end 
        l_end = last_output_element[1]

        # check if current start value is smaller than previous end 
        if start<= l_end:
            # if so then merge, and add the max of last end or current end 
            output[-1][1] = max(l_end, end)
        else:
            # if not, add the start and end as there was no need to merge
            output.append([start,end])

    # return the output 
    return output


def main():
    inpt = [[1,5],[4,6],[6,8],[11,15]]

    ret_val = merge_intervals(inpt)
    print(ret_val)


if __name__ == "__main__":
    main()
