from collections import Counter

def factorial(n):
    if n < 2: return 1
    return n * factorial(n-1)

def hcf(a, b):
    if a == b: return a
    if a == 0: return b
    if b == 0: return a
    if a > b: return hcf(a-b, b)
    return hcf(a, b-a)

def partitions(n, a=[], k=1):
    if n == 0: yield a
    for i in range(k, n+1):
        for ip in partitions(n-i, a+[i], i):
            yield ip

def partition_cycles(ip, n):
    count = factorial(n)
    # f is the frequency of i
    for i, f in Counter(ip).items():
        count //= factorial(f)*i**f
    return count

def solution(w, h, s):
    # Your code here
    numerator = 0
    denominator = factorial(w)*factorial(h)
    for ip_w in partitions(w):
        for ip_h in partitions(h):
            tmp = partition_cycles(ip_w, w)*partition_cycles(ip_h, h)
            factor_sums = sum([sum([hcf(i, j) for i in ip_w]) for j in ip_h])
            numerator += tmp*(s**factor_sums)
    return str(numerator // denominator)