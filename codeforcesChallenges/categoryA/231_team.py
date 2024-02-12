def calculateProblemToChose(problems):
    count = 0

    for _ in problems:
        current_sum = sum(map(int, _))
        if current_sum == 2 or current_sum == 3:
            count += 1

    return count


numberOfProblems = int(input())
listOfProblems = []

for i in range(numberOfProblems):
    problem = input().split()
    listOfProblems.append(problem)

print(calculateProblemToChose(listOfProblems))
