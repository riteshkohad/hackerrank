


# BRUTE FORCE
def maxAreaBruteForce(height: list[int]) -> int:
    # declare variable 
    area = 0
    # loop thru the entire array 
    for l in range(len(height)):
        # second loop from next to the first loop 
        for r in range(l+1, len(height)):

            # calculate width 
            width = r - l 
            # calculate hight 
            higt = min(height[l], height[r])

            # take max of previous area or new width * height 
            area = max(area, width * higt)

    # return area at the end 
    return area



def maxArea(height):
    # declare variables 
    area = 0
    # declare left at the 0 and right pointer at the end of the array 
    l, r = 0, len(height) - 1

    # loop till l remains less than r pointer 
    while l < r:
        # calculate width 
        width = r - l
        # calculate height 
        higt = min(height[l], height[r])

        # calculate area and take max from previous or current one 
        area = max(area, width * higt)

        # check if left pointer is pointing at the smaller array element 
        if height[l] < height[r]:
            # if so then move left to next 
            l += 1
        else:
            # otherwise, move right backward 
            r -= 1

    # return an area at the end 
    return area


def main():
    inpt = [2,3,4,5,18,17,6]
    ret_val = maxAreaBruteForce(inpt)
    print(ret_val)
    ret_val = maxArea(inpt)
    print(ret_val)


if __name__ == "__main__":
    main()