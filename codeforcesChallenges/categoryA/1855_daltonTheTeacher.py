def calculateMoves(n):
    count = 0 # 1oe
    for _ in range(1, len(n) + 1): # n
        if n[_ - 1] == _: # oe
            count = count + 1 # 2oe
    return count # oe


testCases = int(input()) # 2oe

for i in range(testCases):
    nLen = int(input())
    n = list(map(int, input().split())) # 6oe
    moves = calculateMoves(n) # 1oe + comportamiento de la función calculateMoves
    if moves % 2 == 0: # 2oe
        totalMoves = moves // 2 # 2oe
    else:
        totalMoves = moves // 2 + 1 # 2oe
    print(totalMoves) # 1 oe

#Big O = O(n)
