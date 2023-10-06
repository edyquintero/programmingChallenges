def calcularDivisiones(n):
    if n % 2 == 0:
        return (n // 2) - 1
    else:
        return n // 2


pruebas = int(input())

for _ in range(pruebas):
    n = int(input())
    print(calcularDivisiones(n))
