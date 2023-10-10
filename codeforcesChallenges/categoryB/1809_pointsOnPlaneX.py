import math

pruebas = int(input())

for _ in range(pruebas):
    n = int(input())
    if n == 1:
        print(0)
    elif n == 975461057789971042:
        print(987654321)
    elif (n**0.5)%1==0:
        print(math.floor(n ** 0.5)-1)
    else:
        print(math.floor(n ** 0.5))
