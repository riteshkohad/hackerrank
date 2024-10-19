
def removeDuplicates(nums) -> int:
    # declare pointer
    slow = 0

    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
            print(f"replaced: {nums}")
    
    return slow + 1
    


if __name__ == "__main__":
    inpt = [1,1,2,2,3,4,4,5]
    result = removeDuplicates(inpt)
    print(result)