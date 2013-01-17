from math import factorial
x = list(range(10))
i = 1000000-1


# x.insert(2, x.pop(third+2))
periods = [(factorial(len(x)-z))/(len(x)-z) for z in range(len(x))]

def shiftGen(n, periodList, shifts = [], step = [], count = 0):
    if shifts == [] or step == []:
        step = shifts = [0] * len(periodList)
    shifts = zip(step, periodList)
    shifts = map(lambda(x,y): x*y, shifts)
    step[count] = (n - sum(shifts))//periodList[count]
    if count == len(periodList) - 1:
        return step
    return shiftGen(n, periodList, shifts, step,  count + 1)

shifts = shiftGen(i, periods)
print shifts
for n,j in enumerate(x):
    x.insert(n, str(x.pop(shifts[n]+n)))
print ''.join(x)
