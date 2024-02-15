def calculateBanknotes(banknotes, valueToDescompose):
    remainingValue = valueToDescompose

    for denomination in sorted(banknotes.keys(), reverse=True):
        banknotesCount = remainingValue // denomination
        banknotes[denomination] = banknotesCount
        remainingValue -= banknotesCount * denomination

    return banknotes


banknotes = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
valueToDescompose = int(input())
result = calculateBanknotes(banknotes, valueToDescompose)

print(valueToDescompose)

for denomination, count in result.items():
    print(f"{count} nota(s) de R$ {denomination},00")
