#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbersReturn(s):
    # Write your code here
    if len(s) == "1":
        return "NO"
        
    
    cur_count = 1
    prev_num = s[0]
    beautiful_string = "NO"
    min_num = prev_num 
    while cur_count < len(s):
        print(prev_num)
        num = int(prev_num) + 1 
        num_len = len(str(num))
        second_num = int(s[cur_count - 1 : (cur_count -1) + num_len ])
        print(f"second Numb: {second_num}")
        if num == second_num:
            prev_num = str(second_num)
            cur_count = cur_count + num_len
            beautiful_string = "YES"
            cur_count = cur_count + 1
        else:
            # prev_num = str(prev_num) + s[cur_count]
            prev_num = s[:cur_count]
            min_num = prev_num
            
            beautiful_string = "NO"

    ret_val = "NO"
    if beautiful_string == "NO":
        return ret_val
    else: 
        return f"{beautiful_string} {min_num}"

def separateNumbers(s):
    # Write your code here
    if len(s) == "1":
        print("NO")
        return
    
    cur_count = 1
    prev_num = s[0]
    beautiful_string = "NO"
    min_num = prev_num 
    while cur_count < len(s):
        num = int(prev_num) + 1 
        num_len = len(str(num))
        second_num = int(s[cur_count - 1 : (cur_count -1) + num_len ])
        # print(second_num)
        if num == second_num:
            prev_num = str(second_num)
            cur_count = cur_count + num_len
            beautiful_string = "YES"
        else:
            # prev_num = str(prev_num) + s[cur_count]
            prev_num = s[:cur_count]
            min_num = prev_num
            cur_count = cur_count + 1
            beautiful_string = "NO"

    ret_val = "NO"
    if beautiful_string == "NO":
        print(ret_val)
        return
    else: 
        print(f"{beautiful_string} {min_num}") 
        return


if __name__ == '__main__':
    # q = int(input().strip())

    # for q_itr in range(q):
    #     s = input()
    #     separateNumbers(s)

    s = "345346"
    val = separateNumbersReturn(s)
    print(val)
