# Day 2

# Goal: Operators

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    meal_tip = meal_cost + (meal_cost * (tip_percent / 100))
    meal_tip_tax = meal_tip + (meal_cost * (tax_percent / 100))
    print(round(meal_tip_tax))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
