def calculateDivisions(n):
    if n % 2 == 0:
        return (n // 2) - 1
    else:
        return n // 2


testCases = int(input())

for _ in range(testCases):
    n = int(input())
    print(calculateDivisions(n))
