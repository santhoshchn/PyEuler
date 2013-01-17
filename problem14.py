collatzMemo = {1: 1}
def collatz(n, count = 1):
    if not n in collatzMemo:
        if n % 2 == 0:
            collatzMemo[n] = collatz(n//2) + 1
        else:
            collatzMemo[n] = collatz(3*n+1) + 1
    return collatzMemo[n]
    
max = 0
for i in xrange(1,1000000):
    if collatz(i) > max:
        max = collatz(i)
print max

