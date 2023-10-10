import math

testCases = int(input())

for _ in range(testCases):
    chips = int(input())
    result = int(math.sqrt(chips))
    while result * result > chips:
        result -= 1
    while result * result < chips:
        result += 1
    print(result - 1)
