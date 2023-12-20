import re

"""
Time complexity
Since the array is traversed twice, the time complexity of this solution is O(n+n)=O(n), where n is the length of the string.

Space complexity
The space complexity of this solution is O(n), since, at the start of the algorithm we copy it into a list of characters to overcome the issue of strings being immutable in Python.
"""


def reverse_words(sentence):
    # remove extra spaces using regEx lib
    sentence = re.sub(" +", " ", sentence.strip())
    
    # reverse the string using slicing operation 
    rev_sen = sentence[::-1]
    # define start and end pointers 
    start, end = 0, 0
    ret_val = ""

    # loop thru the entire string (reversed one)
    while end <= len(rev_sen) -1:
        # print(len(rev_sen) -1 )
        # print(end)
        # check if end pointer is at the end or value of the end is a space 
        if rev_sen[end] == " " or end == len(rev_sen)-1:
            # take a slice of a word 
            word = rev_sen[start :end+1]
            # print(f"{word} | {start}: {rev_sen[start]} | {end}: {rev_sen[end]}")

            # construct the return value with concatenating the latest work (reverse it)
            ret_val = ret_val + " " + word[::-1]
            # print( ret_val )

            # move the start pointer
            start = end 
        
        # increment the end pointer
        end += 1

    # clean up the return string, remove any additional spaces left 
    ret_val = re.sub(" +", " ", ret_val.strip())

    # return the value
    return ret_val


if __name__ == "__main__":
    input_str = "reverse  these words "
    reversed_val = reverse_words(input_str)
    print(reversed_val)