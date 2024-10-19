

def removeDuplicates(nums) -> int:
    if not nums:
        return 0

    last_element = nums[0]
    dup = 0
    slow = 0

    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
            dup = 0
        else:
            if dup == 0:
                slow += 1
                nums[slow] = nums[fast]
            
            dup += 1

    return slow + 1


if __name__ == "__main__":
    inpt = [1,1,1,2,2,3]
    result = removeDuplicates(inpt)
    print(result)