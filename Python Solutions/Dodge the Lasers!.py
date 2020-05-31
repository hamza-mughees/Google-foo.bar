"""
let r = floor(n(sqrt(2) - 1))
sum(n) = nr + n(n+1)/2 - r(r+1)/2 - sum(r)
"""

import math
# the square root of 2 minus 1, times 10 to the power of 200 (maintaining precision of up to 200 decimal places)
root2m1_200digits = 41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273501384623091229702492483605585073721264412149709993583141322266592750559275579995050115278206057147

def nSum(n):
    return n*(n+1)/2

def recSum(n):
    if n < 2: return n
    
    r = (n*root2m1_200digits)//10**200
    return n*r + nSum(n) - nSum(r) - recSum(r)

def solution(s):
    # Your code here
    s = long(s)
    return str(long(recSum(s)))