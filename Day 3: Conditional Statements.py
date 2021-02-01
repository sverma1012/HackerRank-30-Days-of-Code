# Goal: Conditional Statements

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    if N % 2 != 0: # N is odd
        print('Weird')
    elif (N % 2 == 0) and ((N > 1) and (N < 6)): # If N is even and between 2 and 5
        print('Not Weird')
    elif (N % 2 == 0) and ((N > 5) and (N < 21)): # If N is even and between 6 and 20
        print('Weird')
    else: # If N is even and greater than 20
        print('Not Weird')