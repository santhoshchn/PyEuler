target = 2000000
primeList = [1] * target
primeList[0] = primeList[1] = 0
sum = 0
for (i, prime) in enumerate(primeList):
    if prime:
        sum += i
        for j in xrange(2*i,target,i):
            primeList[j] = 0
print sum





    
    
