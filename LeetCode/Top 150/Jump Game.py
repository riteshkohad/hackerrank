
def canJump(nums) -> bool:
    # total_jumps = len(nums) - 1

    # for i in range(len(nums) - 1, -1, -1):
    #     # print(f"index: {i}, val: {nums[i]}, total jumps: {total_jumps}, sum: {i + nums[i]}")
    #     if i + nums[i] >= total_jumps:
    #         total_jumps = i

    # return True if total_jumps == 0 else False

    total_jumps = 0
    for n in nums:
        print(f"total jumps: {total_jumps}, n: {n} is n > gas {n > total_jumps}")
        if total_jumps < 0:
            return False
        elif n > total_jumps:
            total_jumps = n
        total_jumps -= 1
        
    return True

if __name__ == "__main__":
    inpt = [3,3,1,0,4]
    result = canJump(inpt)
    print(result)