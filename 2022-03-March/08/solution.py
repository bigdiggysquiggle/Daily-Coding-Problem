#!/usr/bin/env python3

#using division

def getProd(numset):
    prod = numset[0]
    for x in numset[1:]:
        prod *= x
    return prod

def makeNewlist(prod, numset):
    newset = []
    for index, val in enumerate(numset):
        newset.append(int(prod / val))
    return newset

#without using division, my first draft version

def makeNoDiv(numset):
    newset = []
    newset.append(int(getProd(numset[1:])))
    i = 1;
    while i < len(numset):
        prod = getProd(numset[:i])
        if (i + 1 < len(numset)):
            prod *= getProd(numset[i + 1:])
        newset.append(int(prod))
        i += 1
    return newset

#without division, second draft after researching the problem

def makeNoDiv(numset):
    newset = []
    tmp = 1
    for i, val in enumerate(numset):
        newset.append(tmp)
        tmp *= val
    tmp = 1
    for i, val in enumerate(reversed(numset)):
        newset[-i - 1] *= tmp
        tmp *= val
    return newset
