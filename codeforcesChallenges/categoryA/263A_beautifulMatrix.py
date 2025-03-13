for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        x, y = i, row.index(1)
        break

moves = abs(x - 2) + abs(y - 2)

print(moves)
