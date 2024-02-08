def calculateVolume(r):
    return (4/3) * 3.14159 * (r**3)


radius = float(input())
print("VOLUME = {:.3f}".format(calculateVolume(radius)))
