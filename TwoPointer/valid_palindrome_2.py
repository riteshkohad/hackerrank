
"""
Time complexity: time complexity of this code is O(n)

Space complexity: space complexity of this code is O(1)
"""

def is_palindrome(s):
    # declare pointers  
    left = 0
    right = len(s) - 1
    mid = len(s) // 2
    mismatch = 0

    # iterate thru the string 
    for x in range(mid):
        # print(f"left: {s[left]} | right: {s[right]}")
        # check if left and right letters are not matching 
        if s[left] != s[right]:
            # adjust the right index by one and check if it matches 
            if s[left] != s[right - 1]:
                # adjust the left index and see if it matches 
                if s[left + 1] != s[right]:
                    # if no combination is matching then return False 
                    return False
                else:
                    # if match found then count the mismatches 
                    mismatch += 1
                    # move the left pointer 
                    left += 1

            else:
                # if match found then count the mismatches 
                mismatch += 1
                # move the right pointer 
                right -= 1

        # for the loop, move both pointers towards middle 
        left += 1
        right -= 1

    # check if mismatches are more than 1
    if mismatch > 1:
        # if so, return false 
        return False

    # if reaches at the end then return True because, except 1 letter, entire string is palindrome 
    return True   


if __name__ == "__main__":
    # print("hello")
    input_str = "dead"
    ret_val = is_palindrome(input_str)
    print(ret_val)