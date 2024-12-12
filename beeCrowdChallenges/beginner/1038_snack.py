inputData = input().split()

def calculateAmount(data):
    code = data[0]
    quanty = float(data[1])
    snacks = {"1": 4.00, "2": 4.50, "3": 5.00, "4": 2.00, "5": 1.50}

    return snacks[code] * quanty

print(f"Total: R$ {calculateAmount(inputData):.2f}")