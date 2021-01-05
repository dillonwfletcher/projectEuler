#!/bin/python3

import sys

# O(n) solution: iterate through range if any number is multiple of 3 or 5
# add to total sum
def On(n):
    s = 0 
    for i in range(1, n):
        if i%3==0 or i%5==0:
            s+=i

    return s

# O(1) solution: find highest multiple of 3, 5, and 15 less than N
# using sum of integer law calculate sum of multiples then find total sum
# sum of integer => n(n+1)/2
def O1(n):
    
    # calculate highest multiple less than N using integer division
    # the // will truncate the result of the division so we get the highest
    # multiple that is a natural number

    # ex: n = 100

    m3 = (n-1)//3 # 99/3 = 33
    m5 = (n-1)//5 # 99/5 = 19.8 => 19
    m15 = (n-1)//15 # 99/15 = 6.6 => 6
    

    # calculate sum of integers for highest multiple of 3, 5, 15
    # multiply sum of integers by 3, 5, 15 respectively
    # add 3sum and 5sum together
    # subtract 15sum to account for double counting
    # to account for rounding errors in cases of large numbers must use bitwise right-shift operator: >>1 is equivalent to division by 2
    return 3*(m3*(m3+1)>>1) + 5*(m5*(m5+1)>>1) - 15*(m15*(m15+1)>>1)


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    
    val = On(n)
    print(val)

    val = O1(n)
    print(val)
