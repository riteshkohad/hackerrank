from collections import deque


"""
Time complexity:
The time complexity of the function Find Maximum in Sliding Window is O(n), where n is the length of the input array nums. 
This is because we iterate through the array once in the for loop, and for each element, we perform constant time operations 
such as appending and popping elements from the deque. The time complexity of the built-in Python functions used in the code, 
such as deque.pop(), deque.append(), and deque.popleft(), is also O(1).

Space complexity:
The space complexity of the function Find Maximum in Sliding Window is O(w), where w is the size of the sliding window. 
This is because we are using a deque to maintain the maximum index in the window, and the deque will store at most w elements. 
Additionally, the output array will also have a maximum of w elements. The space complexity does not include the space used by 
the input array nums.

"""


# function to maintain max location 
def maintain_max_in_queue(current_pointer, queue, nums):
    # loop until queue is not empty and queue contains elements smaller than the current pointer 
    while queue and nums[current_pointer] >= nums[queue[-1]]:
        # if value in the nums array of the current pointer is bigger then 
        # remove the existing index from queue, because current pointer will be added later in the queue 
        queue.pop()


def find_max_sliding_window(nums, w):
    # define output array 
    output = []
    # define de-queue so that we can pop element from either side 
    max_container = deque()

    # loop till window size to keep max index in the queue 
    for i in range(w):
        # call the function to remove all index if value of the current index is higher 
        maintain_max_in_queue(i, max_container, nums)
        # add the current index in the queue 
        max_container.append(i)
    
    # at this point we have only one index in the queue, rest of the indexes were popped out 
    # and the left over index pointing to the max value for the window 
    output.append(nums[max_container[0]])

    # now loop from window size till rest of the array 
    for i in range(w, len(nums)):
        # maintain only max index in the queue 
        maintain_max_in_queue(i, max_container, nums)
        # if it is a first element 
        if max_container and max_container[0] <= (i - w):
            # remove the left one (the first item) from queue if index is not within the window we are working on
            max_container.popleft()
        
        # update the current index as all smaller index have been removed 
        max_container.append(i)
        # update the max value in the output array
        output.append(nums[max_container[0]])

    # return the output array 
    return output

if __name__ == "__main__":
    num_list = [4, 5, 6, 1, 2, 3]
    window_size = 3

    print(find_max_sliding_window(num_list, window_size))