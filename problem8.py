f = open('bignumber.txt', 'rb')
bigNumber = f.read().replace('\n','')

max = 0
for i in xrange(0,996):
    currentProduct = reduce(lambda x,y: x * y, map(int, list(bigNumber[i:i+5])))
    if currentProduct > max:
        max = currentProduct
print max
        
