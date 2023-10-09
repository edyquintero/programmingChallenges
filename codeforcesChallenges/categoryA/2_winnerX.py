scores = {}
maxScore = 0
winner = None
testCases = int(input())

for i in range(testCases):
    name, score = input().split()
    score = int(score)

    if name in scores:
        scores[name] += score
    else:
        scores[name] = score

    if scores[name] > maxScore:
        maxScore = scores[name]
        winner = name
    elif scores[name] == maxScore and winner is None:
        winner = name

print(winner)
