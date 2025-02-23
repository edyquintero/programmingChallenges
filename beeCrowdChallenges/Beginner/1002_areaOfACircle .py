pi = 3.14159

r = float(input())

area = pi * r * r

formatArea = "{:.4f}".format(area).replace(" ", "")

print("A=" + formatArea)
