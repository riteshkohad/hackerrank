
"""
Time complexity:
The time complexity of the function is O(n), where n is the length of the input array nums. This is because the function 
uses the fast and slow pointers pattern to detect a cycle in the array. The pointers traverse the array at different speeds, 
but they are guaranteed to meet at some point if there is a cycle. In the worst case, the pointers will traverse the entire 
array before meeting, resulting in a linear time complexity. The built-in Python functions used in the code, such as indexing 
into the array and comparing values, have constant time complexity and do not affect the overall time complexity of the function.

Space complexity:
The space complexity of the function is O(1) because it uses only a constant amount of extra space. The space complexity of the 
built-in Python functions invoked by the code is not considered in this analysis.
"""


# def find_duplicate(nums):
#     # declare fast and slow pointers
#     slow = 0
#     fast = 0
#     i_iteration = 1 

#     # loop till you find the duplicate 
#     while True:
#         # increment slow by 1
#         slow = nums[slow]
#         # increment fast by 2
#         fast = nums[nums[fast]]

#         print(f"Iteration I: {i_iteration} -> slow: {slow} | fast {fast}")
#         i_iteration += 1

#         # check if slow is matching with fast 
#         if slow == fast:
#             # if so, reset the slow 
#             slow = 0 

#             j_iteration = 0
#             # check for the match again with loop 
#             while True:
#                 # increment slow by 1 
#                 slow = nums[slow]
#                 # increment fast by 1
#                 fast = nums[fast]

#                 print(f"Iteration J: {j_iteration} -> slow: {slow} | fast {fast}")
#                 j_iteration += 1

#                 # if match found that means duplicate found 
#                 if slow == fast:
#                     # return the fast, that is the duplicate 
#                     return fast

#     # Replace this placeholder return statement with your code
    
#     return 0

def find_duplicate(nums):
    fast = slow = nums[0]
  
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow = nums[0]
   
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return fast


if __name__ == "__main__":
    inpt = [1, 5, 4, 3, 2, 4, 6]

    ret_val = find_duplicate(inpt)
    print(ret_val)
