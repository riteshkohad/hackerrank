
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # check if there are any elements in the list, if not , exist with 0
        if not height: return 0

        # declare left and right variables 
        left, right = 0 , len(height) - 1

        # define max left and right 
        mx_left, mx_right = height[left], height[right]
        
        # define water 
        water = 0

        # loop till left is small than right 
        while left < right:
            # print(f"mxL: {mx_left} | mxR: {mx_right} | lf : {left} rt: {right} | water: {water}")

            # if max left is smaller than max right 
            if mx_left < mx_right:
                # if so, move the left pointer 
                left += 1
                # recalculate max left between last max left vs current height 
                mx_left = max(mx_left, height[left])

                # calculate the water by removing current water from max left 
                # used max just to avoid -ve value 
                water += max( mx_left - height[left], 0)
            else:
                # otherwise, move right pointer backwards 
                right -= 1

                # recalculate max right 
                mx_right = max(mx_right, height[right])

                # calculate max by removing current height from max right 
                # max is used just to avoid -ve calculation 
                water += max( mx_right - height[right], 0)
        
        # return water 
        return water


def main():
    inpt = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol = Solution()
    ret_val = sol.trap(inpt)
    print(ret_val)



if __name__ == "__main__":
    main()