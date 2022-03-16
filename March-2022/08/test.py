#!/usr/bin/env python3

import solution

def printRes(numset):
    print("Test set: " + str(numset))
    print("Result:   " + str(solution.makeNewlist(solution.getProd(numset), numset)))
    print("Result:   " + str(solution.makeNoDiv(numset)))

printRes([1, 2, 3, 4, 5])
print()
printRes([3, 2, 1])
