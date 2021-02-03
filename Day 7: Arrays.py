# Goal: Arrays

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    arr2 = arr[::-1] # the resultant array is the reverse of the original array.

    for i in range(len(arr2)):
        print(arr2[i], end=' ') # print out each of the elements of the reversed array.