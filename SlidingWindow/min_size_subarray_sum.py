

"""
Time complexity:
The time complexity of the function is O(n), where n is the length of the input list nums. This is because we iterate through 
the list once using the while loop, and the operations inside the loop have constant time complexity. The built-in Python 
functions used in the code, such as min() and len(), also have constant time complexity.

Space complexity:
The space complexity of the function is O(1) because it only uses a constant amount of extra space to store variables and does not 
allocate any additional data structures. The space complexity of built-in Python functions invoked by the code is not considered 
in this analysis.

"""


def min_sub_array_len(target, nums):
    start, end = 0, 0
    v_sum = 0
    min_sub_len = float("inf")
    
    while end < len(nums):
        v_sum += nums[end]

        while v_sum >= target:
            min_sub_len = min((end + 1) - start, min_sub_len)
            v_sum -= nums[start]
            start += 1
    
        end += 1

    if min_sub_len != float("inf"):
        return min_sub_len

    return 0


if __name__ == "__main__":
    num = [1,4,4]
    trgt = 8

    ret_val = min_sub_array_len(trgt, num)
    print(ret_val)