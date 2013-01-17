f = open('names.txt', 'r')

namesList = f.read().replace('"', '').split(",")
namesList.sort()

totalScore = 0
for (n, name) in enumerate(namesList, start = 1):
    score = 0
    for l in name:
        score += ord(l) - 64
    score *= n
    totalScore += score
print totalScore

