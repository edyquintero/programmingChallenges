def calculateAreaTriangleRectangle(base, height):
    return (base*height)/2


def calculateAreaCircle(radius):
    return 3.14159*(radius**2)


def calculateAreaTrapezium(base1, base2, height):
    return ((base1+base2)*height)/2


def calculateAreaSquare(side):
    return side**2


def calculateAreaRectangle(side1, side2):
    return side1*side2


data = input().split()
A = float(data[0])
B = float(data[1])
C = float(data[2])

print("TRIANGULO: {:.3f}".format(calculateAreaTriangleRectangle(A, C)))
print("CIRCULO: {:.3f}".format(calculateAreaCircle(C)))
print("TRAPEZIO: {:.3f}".format(calculateAreaTrapezium(A, B, C)))
print("QUADRADO: {:.3f}".format(calculateAreaSquare(B)))
print("RETANGULO: {:.3f}".format(calculateAreaRectangle(A, B)))
