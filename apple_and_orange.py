#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_min = s - a 
    orange_min = t - b 
    # print(f"Orange min: {orange_min}")

    apple_count = [x for x in apples if x >= apple_min and x <= (t - a)]
    orange_count = [x for x in oranges if x <= orange_min and x >= (s - b)]
    # print(orange_count)
    # for x in orange_count:
    #     print(f"X: {x} is smaller than orange min {orange_min} and S {s - b} is GT OM: {x < orange_min and (s - b) > orange_min}")
    #     print(f"X: {x} is GT than orange min {orange_min} and S {s - b} is GT OM: {x > orange_min and (s - b) > orange_min}")
    #     print(f"X: {x} is equal to orange min {orange_min} and S {s - b} is GT OM: {x == orange_min and (s - b) > orange_min}")

    print(f"{ len(apple_count)}")
    print(f"{len(orange_count)}")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
