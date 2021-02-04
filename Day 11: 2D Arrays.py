# Goal: Arrays

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maximum = -63

    for row in range(1, 5): # go through each row
        for column in range(1, 5): # go through column
            # add the numbers in the hourglass
            current = arr[row][column] + arr[row - 1][column - 1] + arr[row - 1][column] + arr[row - 1][column + 1] + \
                      arr[row + 1][column - 1] + arr[row + 1][column] + arr[row + 1][column + 1]

            if current > maximum:
                maximum = current

    print(maximum)
