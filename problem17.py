import wolframalpha
f = open('wolframDict.txt', 'w')
wolframDict = {}

client = wolframalpha.Client(open('wolframid', 'r').read())

for i in xrange(1,1001):
    res = client.query(str(i))
    result = res.pods[1]
    print result.text
    wolframDict[i] = result.text

print wolframDict
f.write(str(wolframDict) + '\n')




