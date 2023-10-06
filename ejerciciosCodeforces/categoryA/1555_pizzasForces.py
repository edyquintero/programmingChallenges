def tiempo(nL):
    nPp = nL//6 # 2oe
    pComp = nL%6 # 2oe

    if(nL <= 6): # 1oe
        return 15 # 1oe
    elif(nL==7 or nL == 8): # 3oe
        return 20 # 1oe
    elif (nL == 9 or nL == 10): # 3oe
        return 25 # 1oe

    elif(pComp==5): # 1oe
        return nPp*15 + 15 # 3oe
    elif(pComp==4 or pComp==3): # 3oe
        return nPp*15 + 10 # 3oe
    elif(pComp==1 or pComp==2): # 3oe
        return nPp*15 + 5 # 3oe
    else:
        return nPp*15 # 2oe

pruebas = int(input()) # 2oe

for _ in range(pruebas):
    n = int(input()) # 2oe
    tiempoMinimo = tiempo(n) #Mejor caso --> n=1,2,3,4,5,6 (6oe) Peor caso --> n = 12,18,24... (19oe)
    print(tiempoMinimo) # 1oe
