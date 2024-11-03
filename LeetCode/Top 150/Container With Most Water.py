
def maxArea(height) -> int:
    l, r = 0, len(height) - 1
    max_water = 0
    
    while l < r:
        mw = min(height[l], height[r]) * (r - l)
        max_water = max(max_water, mw)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return max_water


if __name__ == "__main__":
    inpt = [1,8,6,2,5,4,8,3,7]
    result = maxArea(inpt)
    print(result)