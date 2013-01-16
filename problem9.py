print [a*b*c for c in xrange(997,1,-1) for b in xrange(1,c) for a in xrange(1,b) if c**2==a**2+b**2 and a+b+c == 1000]
