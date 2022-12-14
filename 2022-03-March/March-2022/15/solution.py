#!/usr/bin/env python3

def nonAdjSum(arr):
    with_curr = 0
    without = 0
    for each in arr:
        new_without = with_curr if with_curr > without else without
        with_curr = without + each
        without = new_without
    return (with_curr if with_curr > without else without)

if __name__ == "__main__":
    arr = [2, 4, 6, 2, 5]
    print(nonAdjSum(arr))
    arr = [5, 1, 1, 5]
    print(nonAdjSum(arr))
    arr = [5, 5, 10, 100, 10, 5]
    print(nonAdjSum(arr))
