from itertools import product

f = open('numbergrid.txt', 'r')
nList = f.read().rstrip().split('\n')
for (n,list) in enumerate(nList):
    nList[n]=map(int, list.split(' '))
print nList


max = 0
## Horitzontal iterator
for i, j in product(xrange(20), xrange(17)):
    prod = nList[i][j] * nList[i][j+1] * nList[i][j+2] * nList[i][j+3]
    if prod > max:
        max = prod

## Vertical bounds
for i, j in product(xrange(17), xrange(20)):
    prod = nList[i][j] * nList[i+1][j] * nList[i+2][j] * nList[i+3][j]
    if prod > max:
        max = prod

## Forward Diag
for i, j in product(xrange(17), xrange(17)):
    prod = nList[i][j] * nList[i+1][j+1] * nList[i+2][j+2] * nList[i+3][j+3]
    if prod > max:
        max = prod

## Backward Diag
for i, j in product(xrange(17), xrange(19,3,-1)):
    prod = nList[i][j] * nList[i+1][j-1] * nList[i+2][j-2] * nList[i+3][j-3]
    if prod > max:
        max = prod
    
print max
