def calculateFuel(distanceTraveled, travelVelocity):
    return (distanceTraveled*travelVelocity)/12


distance = int(input())
velocity = float(input())

print("{:.3f}".format(calculateFuel(distance, velocity)))
