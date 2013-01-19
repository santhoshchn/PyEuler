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

primesList = primeSieve(1000)
primesList = [x for x in primesList if not (x == 2 or x == 5)]

def mOrder(p):
    k = 1
    while not ((10**k-1) % p == 0):
        k += 1
    return k + 1
max = 0
for i in primesList:
    if mOrder(i) > max:
        max = mOrder(i)
print max

