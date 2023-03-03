#!/usr/bin/env python3

import solution

pair = solution.cons(2, 3)
print("Pair: 2, 3")
print("car(): " + str(solution.car(pair)))
print("cdr(): " + str(solution.cdr(pair)))
