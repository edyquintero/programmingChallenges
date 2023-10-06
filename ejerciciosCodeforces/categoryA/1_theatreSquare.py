import math
insert = input()

numbers = insert.split()

n = int(numbers[0])
m = int(numbers[1])
a = int(numbers[2])

squareHorizontal = math.ceil(n/a)
squareVertical = math.ceil(m/a)

print(squareHorizontal*squareVertical)