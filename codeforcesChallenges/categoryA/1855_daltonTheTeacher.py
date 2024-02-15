def calculateMoves(n):
    count = 0
    for _ in range(1, len(n) + 1):
        if n[_ - 1] == _:
            count = count + 1
    return count


testCases = int(input())

for i in range(testCases):
    nLen = int(input())
    n = list(map(int, input().split()))
    moves = calculateMoves(n)
    if moves % 2 == 0:
        totalMoves = moves // 2
    else:
        totalMoves = moves // 2 + 1
    print(totalMoves)
