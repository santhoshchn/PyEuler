# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

f = open('p13number.txt', 'r')
sum = 0
## Since we only need the first 10 digits of the sum, we only use the
## first 11 digits of each number below
for n in f.read().rstrip().split('\n'):
    sum += int(n[0:11])
print str(sum)[0:10]
