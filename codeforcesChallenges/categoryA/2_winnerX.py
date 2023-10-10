scores = []
maxScore = 0
winner = None
testCases = int(input())

for i in range(testCases):
    name, score = input().split()
    score = int(score)

    if name in scores:
        scores[scores.index(name) + 1] += score
    else:
        scores.append(name)
        scores.append(score)

    if scores[scores.index(name) + 1] > maxScore:
        maxScore = scores[scores.index(name) + 1]
        winner = name
print(winner)