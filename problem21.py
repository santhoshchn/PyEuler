from itertools import combinations

divisionMemo = {}

def primeSieve(n):
    if n == 1:
        return []
    target = int(n)
    primeList = [True] * target
    primeList[0] = primeList[1] = False
    for (i, prime) in enumerate(primeList):
        if prime:
            for j in xrange(2*i,target,i):
                primeList[j] = False
    return [x for (x,y) in filter(lambda (x,y): y == True, enumerate(primeList))]

primesList = primeSieve(10000)

def trialDivision(n, primes):
    if n == 1:
        divisionMemo[1] = [1]
    if not n in divisionMemo:
        prime_factors = []
        for i in primes:
            while n % i == 0:
                prime_factors.append(i)
                n //= i
        divisionMemo[n]=prime_factors
    return divisionMemo[n]

def combinator(nList):
    for s in xrange(1, len(nList) + 1):
        for comb in combinations(nList, s):
            yield comb

def divisors(n):
    return sum(filter(lambda x: x != n, [reduce(lambda x,y: x*y, i) for i in set(combinator(trialDivision(n, primesList)))])) + 1


amicableList = []

for i in xrange(1, 10000):
    sumDivisors = divisors(i)
    if sumDivisors < 10000:
        amicableList.append((i, sumDivisors, divisors(sumDivisors)))
    else:
        continue

sum = 0
for i in filter(lambda (x,y,z): x == z and x != y, amicableList):
    sum += i[0]
print sum

