from datetime import date
sum = 0
for i in xrange(1901, 2001):
    for j in xrange(1, 13):
        if date(i, j, 1).weekday() == 6: sum += 1
print sum
