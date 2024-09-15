from collections import deque

def find_max_sliding_window(nums, w):
    # this will hold indexes because we will have to slide window by left & right index, so when left window 
    # goes out of sight, we need to remove that index from Dequeue, if we keep value we will not know what 
    # index that value belongs to, we will miss the window 
    que = deque()   
    output = []
    l = r = 0

    while r < len(nums):
        # before adding new index to the queue, make sure all existing smaller value indexes are removed from queue
        while que and nums[que[-1]] < nums[r]:
            que.pop()

        # add current index in the queue but before adding remove the all small values
        # so that only index of max value will be in the queue
        que.append(r)

        # check the left side pointer, if it is greater that means our window has passed the 
        # left most queue value, so we dont have to keep that index anymore
        # queue will always have index of the current window's max element 
        if l > que[0]:
            que.popleft()
        
        # check the window size 
        # as soon as window is sliding, add the left most value from dequeue (which is the index of max value of the window)
        # and add it to the queue 
        if (r+1) >= w:
            output.append(nums[que[0]])
            l += 1

        r += 1

    return output






if __name__ == "__main__":
    ary = [1,2,3,4,5,6,7,8,9,10]
    n = 3
    val = find_max_sliding_window(ary, n)
    print(val)