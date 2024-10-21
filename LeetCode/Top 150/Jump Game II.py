

def jump(nums) -> int:
    l, r = 0, 0
    total_jumps = 0

    while r < len(nums) - 1:
        max_jump = 0
        for i in range(l, r +1):
            max_jump = max(max_jump, i + nums[i])

        l = r + 1
        r = max_jump
        total_jumps += 1
    
    return total_jumps



if __name__ == "__main__":
    inpt = [2,3,1,1,4]
    result = jump(inpt)
    print(result)