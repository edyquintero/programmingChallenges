import math


def calculateDistance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


pointX1, pointY1 = map(float, input().split())
pointX2, pointY2 = map(float, input().split())

print("{:.4f}".format(calculateDistance(pointX1, pointY1, pointX2, pointY2)))
