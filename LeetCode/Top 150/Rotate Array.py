
def reverse(nums, start, end):
    while start <= end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    
    return nums

def rotate(nums, k: int) -> None:
    if k == 0:
        return 

    k = k % len(nums)

    start, end = 0, len(nums) - 1
    nums = reverse(nums, start, end)

    start, end = 0, k-1
    nums = reverse(nums, start, end)
    
    start, end = k, len(nums) - 1
    nums = reverse(nums, start, end)

    print(nums)


if __name__ == "__main__":
    inpt = [1,2]
    v = 3
    result = rotate(inpt, v)
    print(result)