# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 
from math import fabs

numberList = xrange(1,21)

#Finds GCD using Euclidean algorithm
def gcd(x, y):
    x = int(x)
    y = int(y)
    while y:
        x,y = y,x%y
    return x

def lcm(a, b):
    return fabs(a*b)//gcd(a, b)

print reduce(lcm, numberList)
