def get_next_element(i, nums, cur_dir):
    # i is a current index we need to move whatever value of the array at the i th position forward/backward 
    # so we are adding nums[i] to the index 
    # but this could make new position out of the array bounds 
    # so we will % it by size of the array so that remainder will be within the array limit and it will go back as a cycle
    # ex. if array has 5 elements and we mod it by 5 (5 % 5 = 0) but if we get new index say 7 so we will do 7 % 5 = 2, it will go back to the array 

    # get the next element by % with length of array 
    nxt_pos = (nums[i] + i) % len(nums)

    # check the next direction 
    nxt_dir = 1 if nums[nxt_pos] > 0 else -1

    # if current direction and next are not the same and 
    # current index (i) and next index (nxt_pos) are the same means cycle detected with just 1 value 
    if cur_dir != nxt_dir or i == nxt_pos:
        return -1 

    return nxt_pos


def circular_array_loop(nums):
    slow = fast = 0

    for i in range(len(nums)):
        # this check is to see if current element is 0 dont process
        # this saves time and makes code run in O(n) time otherwise it will take O(n^2)
        if nums[i] == 0:
            continue

        # reset the slow and fast pointer every time 
        slow = fast = i 

        # check the current direction of the flow
        current_direction = 1 if nums[i] > 0 else -1


        # set the loop 
        while True:
            # move slow pointer once 
            slow = get_next_element(slow, nums, current_direction)

            # fast pointer to move twice as fast so this is first and below is the second move
            fast = get_next_element(fast, nums, current_direction)

            # before we try to move our fast pointer its second move, check if it is repeating 
            if slow == -1 or fast == -1:
                break

            # move the fast pointer 2nd time 
            fast = get_next_element(fast, nums, current_direction)
            if fast == -1:
                break

            # cycle detected 
            if fast == slow:
                return True

        # at the end of the loop, mark current i element as processed by replacing its value to 0
        nums[i] = 0

    # if no cycle detected, return False at the end 
    return False



if __name__ == "__main__":
    ary = [3,3,1,-1,2]
    val = circular_array_loop(nums=ary)
    print(val)
