#!/bin/python3

import sys


def euler2(n):
    # O(n) solution
    # generate a list of even #s of fibonacci sequence that does not exceed N
    x, y = 1, 2
    fib = []
    while x < n:

        # check for even value
        if x % 2 == 0:

            # add term to fibonacci seq
            fib.append(x)

        # calculate next term
        tmp = y
        y = x + y
        x = tmp
    
    # return sum of even values of fibonaccis seq
    return sum(fib)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    val = euler2(n)

    print(val)
