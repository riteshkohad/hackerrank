
"""
Time complexity:
The time complexity of this function is O(n), where n is the length of the input string. This is because we iterate through 
the string once using a sliding window approach, and each iteration takes constant time. The built-in Python functions used 
in this code, such as checking for membership in a dictionary and finding the maximum value, also have constant time complexity.

Space complexity:
The space complexity of the function “Longest Substring without Repeating Characters” is O(n), where n is the length of the input 
string. This is because we are using a hashmap to store the characters and their indices, which can take up to O(n) space in the 
worst case. Additionally, we are using a few variables to keep track of the start and end indices, which take constant space. 
The built-in Python functions invoked by the code do not significantly affect the space complexity.
"""



def find_longest_substring(input_str):
    hashMap = {}
    start, end = 0, 0
    max_len = 0

    for end in range(len(input_str)):
        print(hashMap)
        if input_str[end] not in hashMap:
            hashMap[input_str[end]] = end
            # max_len += 1
        else:
            max_len = max(end - start, max_len)  
            start = end + 1

    max_len = max(end - start, max_len) 
    return max_len


if __name__ == "__main__":
    # print("hello")
    str = "pwwkew"
    ret_val = find_longest_substring(str)
    print(ret_val)