s = input().strip()
t = input().strip()

row_diff = int(t[1]) - int(s[1])
col_diff = ord(t[0]) - ord(s[0])

num_moves = max(abs(row_diff), abs(col_diff))

print(num_moves)

for _ in range(num_moves):
    move = ""

    if col_diff > 0:
        move += "R"
        col_diff -= 1
    elif col_diff < 0:
        move += "L"
        col_diff += 1
    if row_diff > 0:
        move += "U"
        row_diff -= 1
    elif row_diff < 0:
        move += "D"
        row_diff += 1

    print(move)
