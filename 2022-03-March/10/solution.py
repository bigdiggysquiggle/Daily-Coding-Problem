#!/usr/bin/env python3

def negFilter(li):
    neg = 0
    for ind, val in enumerate(li):
        if (val <= 0):
            li[neg], li[ind] = li[ind], li[neg]
            neg += 1
    return li[neg:]

def markExisting(li):
    print(len(li) - 1)
    for val in li:
        print('check ' + str(val))
        if (val < len(li)):
            li[val] = -li[val]
        print(li)

def findMissingPos(li):
    filt = negFilter(li)
    markExisting(filt)
    for ind, val in enumerate(filt):
        if (val > 0):
            return ind + 1
    return len(filt) + 1
