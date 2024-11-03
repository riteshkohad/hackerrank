
def threeSum(nums):
    if not nums:
        return []
    
    nums = sorted(nums)
    print(nums)
    output = []
    l, r = 0, len(nums) - 1

    for i, num in enumerate(nums):
        # to remove duplicate back to back numbers
        if i >0 and num == nums[i-1]:
            continue

        l = i + 1
        r = len(nums) - 1
        while l < r:
            tot = num + nums[l] + nums[r]
            # print(f"val: {val}, tot: {tot}, num:{num}")
            if tot == 0:
                output.append([num, nums[l], nums[r]])
                l += 1
                
                # skip same numbers
                while nums[l] == nums[l-1] and l < r:
                    l += 1
            elif tot < 0:
                l += 1
            else:
                r -= 1

    return output



if __name__ == "__main__":
    inpt = [-1,0,1,2,-1,-4]
    result = threeSum(inpt)
    print(result)