def newNumber(number):
    i = 0
    num = 1
    while i < number:
        if not (num % 3 == 0 or num % 10 == 3):
            i += 1
        num += 1
    return num - 1


testCases = int(input())

for i in range(testCases):
    number = int(input())
    result = newNumber(number)
    print(result)
