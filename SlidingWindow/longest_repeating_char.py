

"""
Time complexity:
The time complexity of the function Longest Repeating Character Replacement is O(n), where n is the length of the input string s. 
This is because we iterate through the string once using a while loop, and each iteration takes constant time. The built-in Python 
functions used in the code, such as max(), are also O(1) operations. Therefore, the overall time complexity is O(n).

Space complexity:
The space complexity of the function Longest Repeating Character Replacement is O(1). This is because the space used by the 
function does not depend on the size of the input string. The function only uses a constant amount of space to store variables 
such as min_len, start, counter, i, and most_freq_char. The space complexity of the built-in Python functions invoked by the 
code is also O(1) as they do not use additional space proportional to the input size. Even hash map can take max of const 26 chars
"""

def longest_repeating_character_replacement(s, k):
    min_len = 0
    start = 0
    counter = {}
    i = 0
    most_freq_char = 0

    while i < len(s):
        print(counter)

        if s[i] in counter:
            counter[s[i]] = counter[s[i]] + 1
        else:
            counter[s[i]] = 1

        most_freq_char = max(most_freq_char, counter[s[i]])
        
        
        if i - start + 1 - most_freq_char > k:
            counter[s[start]] -= 1
            start += 1

        i += 1
    
    min_len = max(i - start, min_len)
    
    return min_len

if __name__ == "__main__":
    inp_str = "aaacbbbaabab"
    chars = 2
    ret_val = longest_repeating_character_replacement(inp_str, chars)
    print(ret_val)

    # t = {"a": 1, "b": 2}

    # if "c" in t:
    #     t["c"] = t["c"] + 1
    # else:
    #     t["c"] = 1
    
    # print(t)