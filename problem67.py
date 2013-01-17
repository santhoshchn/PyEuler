f = open('triangle.txt', 'r')
triangle = f.read().rstrip()
triangle = map(lambda x: map(int, x.split(" ")), triangle.split("\n"))[::-1]
for (x, y) in [(x,y) for x in range(1, len(triangle)) for y in range(len(triangle)-x)]:
    triangle[x][y] += max(triangle[x-1][y], triangle[x-1][y+1])
print triangle[-1]



