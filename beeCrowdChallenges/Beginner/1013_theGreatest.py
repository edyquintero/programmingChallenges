def calculateTheGreatest(num1, num2, num3):
    return max(num1, num2, num3)


numbers = input().split()
A = int(numbers[0])
B = int(numbers[1])
C = int(numbers[2])

print(f"{calculateTheGreatest(A, B, C)} eh o maior")
