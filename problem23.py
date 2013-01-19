

def divisors(n):
    sum = 1
    for i in xrange(2, int(n**0.5) + 1):
        if n % i == 0:
            sum += i + n/i
    if int(n**0.5) == n**0.5:
        sum -= n**0.5
    return sum

upperLimit = 28123
naSum = 0
abundantNumbers = set()
for i in xrange(1, upperLimit):
    if divisors(i) > i:
        abundantNumbers.add(i)
    if not any((i-x in abundantNumbers) for x in abundantNumbers):
        naSum += i
print naSum
        
