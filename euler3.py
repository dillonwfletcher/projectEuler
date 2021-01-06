#!/bin/python3

import math

def euler3(n):
    
    # if n < 2 then no prime factors exist; 1 is not considered a prime number
    if n < 2:
        return "Largest Prime Factor Does Not Exist"

    # if N is even repeatedly divide by 2
    while n % 2 == 0: 

        n = n // 2

    # if N becomes 1 then 2 is largest prime number
    if n == 1: 
        return 2 #largest prime number


    # we know know that N is an odd number
    # starting at 3, increment by 2 since there are no even factors for an odd number until we reach sqrt(N)
    # we go to sqrt(N) to reduce length of loop; going to N or sqrt(N) has no impact on results
    for i in range(3, int(math.sqrt(n)+1), 2):

        # if N is divisible by i, divide N by i
        # this step will eliminate all composite numbers
        while n % i == 0:
            n = n // i

            x = i

    # if N > 2 then return N as largest prime number else return highest value of i as largest prime number
    if n > 2:
        return n
    else:
        return x

# below is for testing purposes
# t is the number of cases wanted to be tested
# for each case ask user for N
# This solution should return largest prime factor for all integers N > 1
# Testing was conducted on integers N in [2, 10^12]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())


    val = euler3(n)
    print(val)
