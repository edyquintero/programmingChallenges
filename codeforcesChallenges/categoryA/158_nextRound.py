def calculateAdvance(score, scores):
    advanced = 0
    
    for _ in scores:
        if _ >= scores[score - 1] and _ != 0:
            advanced += 1

    return advanced


participants, scoreBase = map(int, input().split())
participantsScores = list(map(int, input().split(' ')))
print(calculateAdvance(scoreBase, participantsScores))
