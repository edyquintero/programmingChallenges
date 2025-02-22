def calculateConsumption(distanceTotal, fuelSpent):
    return distanceTotal/fuelSpent


distance = int(input())
fuel = float(input())

print("{:.3f}".format(calculateConsumption(distance, fuel)) + " km/l")
