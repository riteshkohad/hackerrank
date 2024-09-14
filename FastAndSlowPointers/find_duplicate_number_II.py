
def find_duplicate(nums):
    fast = slow = 0

    for i in range(len(nums) ):
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            slow = 0
            for j in range(len(nums)):
                slow = nums[slow]
                fast = nums[fast]

                if slow == fast:
                    return fast
    
    return 0

if __name__ == "__main__":
    ary = [2,2,1]
    val = find_duplicate(ary)
    print(val)