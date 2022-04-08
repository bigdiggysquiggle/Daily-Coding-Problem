#!/usr/bin/env python3

def climb(stair, steps=[1, 2]):
    total = 0
    if not stair:
        return 1
    for step in steps:
        if stair >= step:
            total += climb(stair - step, steps)
    return total

if __name__ == '__main__':
    print(climb(4))
    print(climb(12, [1, 3, 5]))
