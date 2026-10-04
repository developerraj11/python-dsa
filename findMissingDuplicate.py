# write a program that accept an array with length n as 2nd parameter, having exactly 1 duplicate 
# value, need to return this duplicate and in place of this missing number with best time complexity and 
# space complexity

# You are given an array of ‘N’ integers where each integer value is between ‘1’ and ‘N’. Each integer appears exactly once except for ‘P’, which appears exactly twice, and ‘Q’, which is missing. Your task is to find ‘P’ and ‘Q’ and return them respectively.

from ast import For
import numbers
from pdb import run


def find_duplicate_missing(a):
    seen = set()
    duplicate = -1

    for num in a:
        if num in seen:
            duplicate = num
        seen.add(num)

    missing = -1

    for num in range(1, len(a) + 1):
        if num not in seen:
            missing = num
            break

    return duplicate, missing