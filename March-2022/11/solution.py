#!/usr/bin/env python3

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def front(a, b):
        return a
    return pair(front)

def cdr(pair):
    def back(a, b):
        return b
    return pair(back)
