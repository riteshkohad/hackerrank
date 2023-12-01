#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2:] == "AM":
        if s[:2] == "12":
            return f"00{s[2:-2]}"
        else:
            return s[:-2]
    elif s[-2:] == "PM":
        if s[:2] == "12":
            return s[:-2]
        else:
            return f"{int(s[:2]) + 12}{s[2:-2]}"


if __name__ == '__main__':
    # s = input()
    s = "12:59:00AM"
    result = timeConversion(s)

    print(f"{result}")

    