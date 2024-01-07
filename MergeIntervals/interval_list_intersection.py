

"""
Time complexity: The time complexity of the function Interval List Intersections is O(n + m), where n is the length of 
interval_list_a and m is the length of interval_list_b. This is because we iterate over both lists once, comparing each 
interval with the intervals in the other list. The built-in Python functions used in the code, such as len() and append(), 
have a time complexity of O(1) and do not significantly affect the overall time complexity.

Space complexity: The space complexity of the function Interval List Intersections is O(1) because the space used by the function 
does not depend on the size of the input lists. The function only uses a constant amount of space to store the output array and 
the two pointers. The built-in Python functions invoked by the code, such as len() and append(), also have constant space 
complexity.
"""

def intervals_intersection(interval_list_a, interval_list_b):
    # declare a variable for output
    output = []

    # declare two pointers to track list a and b
    a_ptr, b_ptr = 0,0 

    # Iterate over the lists until any of the list reaches at the end
    while a_ptr < len(interval_list_a) and b_ptr < len(interval_list_b):
        # unpack stat and end of each interval from each list 
        a_start, a_end = interval_list_a[a_ptr]
        b_start, b_end = interval_list_b[b_ptr]

        # check if there is an intersection 
        if a_start <= b_end and b_start <= a_end:
            # if so, add the intersection to the output array 
            # intersection will be the max of the starting of each array 
            # end will be the min of ending of each array 
            output.append([max(a_start, b_start), min(a_end, b_end)])
        
        # if end of B list is smaller then move b_ptr
        if a_end > b_end:
            b_ptr += 1
        # if end of A list is smaller then move a_ptr
        elif a_end < b_end:
            a_ptr += 1
        # otherwise, move moth a and b ptrs
        else:
            a_ptr += 1
            b_ptr += 1

    # return the output 
    return output



def main():
    list_a = [[1, 3], [5, 6], [7, 8], [9, 10], [12, 15]] 
    list_b = [[2, 4], [7, 10]]
    ret_val = intervals_intersection(list_a, list_b)

    print(ret_val)


if __name__ == "__main__":
    main()