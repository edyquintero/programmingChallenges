def calcularMovimientos(n):
    count = 0 #1oe
    for i in range(1, len(n) + 1): #n
        if n[i - 1] == i:
            count = count + 1
    return count

pruebas = int(input()) #2oe

for i in range(pruebas):
    nLen = int(input()) #2oe
    n = list(map(int, input().split())) #4oe
    movimientos = calcularMovimientos(n) #1oe + complejidad de calcularMovimientos
    if movimientos % 2 == 0: #2oe
        movimientosTotales = movimientos // 2 #2oe
    else:
        movimientosTotales = movimientos // 2 + 1 #3oe
    print(movimientosTotales) #1oe

#n**2