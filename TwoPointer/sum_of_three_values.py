

"""
Time complexity:
The time complexity of the function “find_sum_of_three” is O(n^2), where n is the length of the input 
array “nums”. This is because we have a nested loop structure, where the outer loop iterates through each 
element in the array, and the inner loop iterates through the remaining elements. The sorting operation has 
a time complexity of O(n log n), but it does not significantly affect the overall time complexity. The built-in 
Python functions used in the code, such as “sort” and “len”, have a time complexity of O(n log n) and O(1) 
respectively.
------------------
Space complexity:
The space complexity of the function “find_sum_of_three” is O(1) because it only uses a constant amount of 
extra space for variables such as “cur_pos”, “low”, and “high”. The space complexity does not depend on the 
size of the input array.

The space complexity of the “two_pointers” function is also O(1) because it only uses a constant amount of 
extra space for variables “left” and “right”. The space complexity does not depend on the size of the input array.

sorting will take from range O(log n) to O(n) depending on the which sort algorithm is used. for builtin sort()
O(n) is the space complexity  

"""


def find_sum_of_three(nums, target):
   # Replace this placeholder return statement with your code
    # sort the array
    nums.sort()
    # print(nums)

    # mark the current position 
    cur_pos = 1

    # iterate thru the array
    for x in nums:
        # take the low and high values of array (two pointers), low should be next to the x element 
        low = cur_pos
        high = len(nums) - 1

        # move the two pointers
        while low < high:

            # calculate the sum of x, low, and high 
            # print(f"Cur_pos: {cur_pos} | X: {x} | low: {nums[low]} | high: {nums[high]}")
            cur_sum = x + nums[low] + nums[high]
            
            # check if sum is matching with target 
            if cur_sum == target:
                return True
            elif cur_sum > target:
                # sum is high then move the high pointer backwards 
                high = high - 1
            elif cur_sum < target:
                # if sum is low then move low pointer to forward 
                low = low + 1
            # print("-" * 10)
             
        # move the current pointer with for loop to have next value 
        cur_pos = cur_pos + 1

    return False

if __name__ == "__main__":
    nums = [3,7,1,2,8,4,5]
    target = 21
    result = find_sum_of_three(nums, target)
    print(f"Are there three values which sums to {target}: {result}")