
def binary_search(nums, target):
    # 1. check if only one element exists in the list, check and return 
    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    # 2. define start, end and middle elements 
    s, e = 0, len(nums) -1 
    m = s + ((e - s) // 2)

    # 3. loop until start is <= end
    while s <= e:
        # 3.1 if nums of middle is == target return middle 
        if nums[m] == target:
            return m
        else:
            # 3.2 adjust the start and end pointers based on the target
            if nums[m] < target:
                # if middle of nums is smaller than target move start towards middle + 1
                s = m + 1
            else:
                # otherwise move end towards middle - 1
                e = m - 1
            
            # recalculate middle 
            m = s + ((e - s) // 2)

    return -1



if __name__ == "__main__":
    inpt = [11]
    target = 11
    result = binary_search(inpt, target)
    print(result)