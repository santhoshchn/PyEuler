fibSeq = []
def fib(n):
    if n < 1:
        return
    elif n == 1 or n == 2:
        fibSeq.append(1)
    else:
        fibSeq.append(fibSeq[-1] +
                      fibSeq[-2])
        
i = 1
while True:
    fib(i)
    if len(str(fibSeq[-1])) >= 1000:
        print i
        break
    i += 1
