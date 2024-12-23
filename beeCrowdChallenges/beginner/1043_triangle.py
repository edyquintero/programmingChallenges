sides = input().split()

A = float(sides[0])
B = float(sides[1])
C = float(sides[2])

perimeter = lambda x, y, z: x + y + z
area = lambda x, y, z: ((x + y) * z) / 2

if (A + B > C) and (A + C > B) and (B + C > A):
    print(f"Perimetro = {perimeter(A, B, C):.1f}")
else:
    print(f"Area = {area(A, B, C):.1f}")
