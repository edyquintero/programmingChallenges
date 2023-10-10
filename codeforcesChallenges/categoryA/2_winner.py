testCases = int(input())

winners = [""] * (testCases + 1)
points = [0] * (testCases + 1)

for _ in range(1, testCases + 1):
    name, add_points = input().split()
    points[_] = int(add_points)
    winners[_] = name

players = set(winners[1:])

state = {}
for player in players:
    state[player] = [0] * (testCases + 1)

for _ in range(1, testCases + 1):
    for player in players:
        state[player][_] = state[player][_ - 1]
    state[winners[_]][_] += points[_]

maxScore = max(state[player][testCases] for player in players)

finalWinner = ""
for _ in range(1, testCases + 1):
    if finalWinner:
        break
    for player in players:
        if state[player][_] >= maxScore and state[player][testCases] == maxScore:
            finalWinner = player
            break

print(finalWinner)
