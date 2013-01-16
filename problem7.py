# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
from math import sqrt
target = 10001
i = 0
primeCount = 0

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in xrange(3,int(sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

while True:
    if isPrime(i):
        primeCount +=1
        if primeCount == target:
            print i
            break
        i += 1
    else:
        i += 1
