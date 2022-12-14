#!/usr/bin/env python3

import time

def scheduler(f, n):
    time.sleep(float(n) / 100) # convert to milliseconds
    f()

if __name__ == '__main__':
    scheduler(lambda : print("butts lol"), 1000)
