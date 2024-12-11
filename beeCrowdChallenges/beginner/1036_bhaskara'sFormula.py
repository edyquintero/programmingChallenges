data = input().split()
a = float(data[0])
b = float(data[1])
c = float(data[2])

def calcatateBhaskara(a, b, c):
    root = b**2 - 4*a*c
    denominator = 2*a
    if denominator != 0 and root > 0:
        r1 = (-b + root ** 0.5) / denominator
        r2 = (-b - root ** 0.5) / denominator
        print(f"R1 = {r1:.5f}")
        print(f"R2 = {r2:.5f}")
    else:
        print("Impossivel calcular")

calcatateBhaskara(a, b, c)
