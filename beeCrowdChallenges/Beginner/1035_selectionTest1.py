data = input().split()
A = float(data[0])
B = float(data[1])
C = float(data[2])
D = float(data[3])

if (B > C) and (D > A) and ((C + D) > (A + B)) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")