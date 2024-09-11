def find_sum_of_three(nums, target):
    nums.sort()

    for i, val in enumerate(nums):
        # print(f"Number: {val} is at:{i} index")
        low = i + 1
        high = len(nums) - 1 

        while low < high:
            total = val + nums[low] + nums[high]

            if total == target:
                return True
            elif total > target:
                high -= 1
            elif total < target:
                low +=1
    return False


if __name__ == "__main__":
    arr = [3,7,1,2,8,4,5]
    total = 10
    result = find_sum_of_three(arr, total)
    print(result)