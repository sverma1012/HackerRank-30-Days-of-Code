# Goal: Binary Numbers

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    binary = bin(n)[2:]
    current = 0
    max = 0

    for i in range(len(binary)):
        if binary[i] == '1': # check if the value is one
            current += 1 # if so, increase the current count by one
            if current > max: # if current count is larger than max count, then make max equal to current
                max = current
        else: # if the value is zero
            current = 0 # then make the current count zero. Max count remains the same.


    if max > current:
        print(max)
    else:
        print(current)