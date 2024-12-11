value = float(input())

if 0 < value < 1000000:
    valueInCents = int(value * 100)

    print('NOTAS:')
    for i in [10000, 5000, 2000, 1000, 500, 200]:
        print('%d nota(s) de R$ %.2f' % (valueInCents // i, i / 100))
        valueInCents %= i

    print('MOEDAS:')
    for i in [100, 50, 25, 10, 5, 1]:
        print('%d moeda(s) de R$ %.2f' % (valueInCents // i, i / 100))
        valueInCents %= i
