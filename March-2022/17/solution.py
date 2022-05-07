#!/usr/bin/env python3

import re

def getmatch(lst, quer):
	newlst=[x for x in lst if x.startswith(quer)]
	return newlst

if __name__ == "__main__":
    lst=["dog", "deer", "deal"]
    print(lst)
	print(getmatch(lst, "de"))
    lst=["test", "sock", "bean", "string", "cheese", "toast", "shoe", "floor", "stove"]
	print(getmatch(lst, "s"))
