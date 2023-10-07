def tiempo(friends):
    friends // 6
    pizza = friends % 6

    if friends <= 6:
        return 15
    elif friends == 7 or friends == 8:
        return 20
    elif friends == 9 or friends == 10:
        return 25

    elif pizza == 5:
        return friends * 15 + 15
    elif pizza == 4 or pizza == 3:
        return friends * 15 + 10
    elif pizza == 1 or pizza == 2:
        return friends * 15 + 5
    else:
        return friends * 15


testCases = int(input())

for _ in range(testCases):
    friends = int(input())
    minTime = tiempo(friends)
    print(minTime)
