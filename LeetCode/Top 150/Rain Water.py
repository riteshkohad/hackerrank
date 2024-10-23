
def trap(height) -> int:
    l, r = 0, len(height)-1
    max_l, max_r = height[0], height[-1]
    water = 0

    while l < r:
        if max_l < max_r:
            l += 1
            max_l = max(max_l , height[l])
            water += max_l - height[l]
        else:
            r -= 1
            max_r = max(max_r, height[r])
            water += max_r - height[r]
    
    return water


if __name__ == "__main__":
    inpt = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = trap(inpt)
    print(result)