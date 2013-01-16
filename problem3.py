from math import sqrt, ceil

targetNumber = 600851475143

def largestPrime(n):
    for i in xrange(2, int(ceil(sqrt(n)))):
       # print i
        if n % i == 0:
            #print "Divided"
            return largestPrime(n/i)
    else:
        print n

largestPrime(targetNumber)
