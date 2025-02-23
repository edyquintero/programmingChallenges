numbers = input().split()

A = int(numbers[0])
B = int(numbers[1])

if A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
