
def jump_game(nums):
    # Declare target where to reach 
    target = len(nums) - 1

    # loop from backwards and see if current index + value of current index is >= target
    # if yes, then assign current index as a new target 
    for i in range(len(nums) -1, -1, -1):
        if i + nums[i] >= target:
            target = i
            
    # if target is 0 that means we successfully traveled at the beginning of the array
    # hence return True
    return True if target == 0 else False 


if __name__ == "__main__":
    inpt = [0]
    result = jump_game(inpt)
    print(result)