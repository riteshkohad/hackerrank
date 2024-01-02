
"""
Time complexity: 
The time complexity of the function min_window is O(n), where n is the length of the input string str1. 
This is because the function iterates through the characters of str1 once using a while loop. The time 
complexity of the function reconfirm_window is O(m), where m is the length of the subsequence str2. This is 
because the function iterates through the characters of str2 once using a for loop. The overall time complexity 
of the code is O(n + m), which can be simplified to O(n) since n is typically larger than m.
but the worst case time complexity is O(n * m) if str1 = "aaaaaaa" and str2 = "aa"

Space complexity:
The space complexity of the function Minimum Window Subsequence is O(1) because it uses a constant amount of extra space. 
The function does not create any additional data structures or use any built-in Python functions that would significantly 
increase the space complexity.

"""


def reconfirm_window(s, e, s1, s2):
    # print(f"{s} {e} {s1} {s2}")
    # take a length and declare variables 
    str2_len = len(s2)
    str2_char = str2_len - 1
    start = 0

    # loop in reverse END to START by -1 increment 
    for i in range(e, s-1, -1):
        # print(f"reverse {s1[i]} == {s2[str2_char]} ?")
        # check if last char of the search string and search window is matching 
        if s1[i] == s2[str2_char]:
            # if so, search the previous char from search string 
            str2_char -= 1

        # print(f"is {str2_char} < 0 ?")
        # check if all the chars in the search string has been found 
        if str2_char < 0:
            # print(f"Yes {s1[i:e+1]}")
            # take the new start and end and slice the string 
            output = s1[i:e+1]
            # return output 
            return output

def min_window(str1, str2):
    # declare variables 
    output = ""
    start = 0
    start_found = False
    end = 0

    str2_char = 0 
    str2_len = len(str2)
    i = 0

    #  loop till end of the input string 
    while i < len(str1):
        # print(f"is {str1[i]} == {str2[str2_char]}?")
        # check if char of input string and the string to search are matching
        if str1[i] == str2[str2_char]:
            # print(f"Yes")
            # if match then increase the index of search string 
            str2_char += 1

            # check if first char is found 
            if start_found == False:
                # if so, mark the starting point for the window and turn the flag
                start = i 
                start_found = True

            # check if all the chars in the search string is found 
            if str2_char == str2_len: 
                # if so, mark the window end position 
                end = i
        
        # confirm the start and end locations are found 
        if end >= str2_len - 1 and str2_char == str2_len:
            # check the chars from start and end position and reconfirm the 
            # letters in a search string iterating in reverse so that any extra chars at the begging will be removed   
            final_string = reconfirm_window(start, end, str1, str2)
            # print(f"final string: {final_string}")
            # move the starting pointer 
            i = end - (len(final_string) - 1 ) 
            # print(f"reset i {i}")
            # reset the variable so that we can find the beginning of the string 
            start = 0
            start_found = False
            end = 0
            str2_char = 0

            # print(f"is {len(output)} > 0 and {len(output)} > {len(final_string)}")
            # check if the output variable has any string 
            if len(output) > 0: 
                # if yes, check if existing is longer
                if len(output) > len(final_string):
                    # if so, replace the smaller string in the output variable 
                    output = final_string 
            else:
                # if no, add the final string to output variable 
                output = final_string 
        # move the pointer 
        i += 1

    # return output 
    return output



if __name__ == "__main__":
    string1 = "abcdbebe"
    string2 = "bbe"

    ret_val = min_window(string1, string2)
    # ret_val = reconfirm_window(1, 5, "adf", "adsf")
    print(ret_val)
