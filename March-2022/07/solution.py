#!/usr/bin/env python3

def numcheck(nums, val):
    for index, num in enumerate(nums):
        for in2, test in enumerate(nums[index + 1:]):
            if (num + test) == val:
                return True
    return False
