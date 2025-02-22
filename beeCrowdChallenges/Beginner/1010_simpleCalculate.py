def calculateValueToPay(amountProd1, priceProd1, amountProd2, priceProd2):
    return amountProd1*priceProd1 + amountProd2*priceProd2


line1 = input().split()
amount1 = int(line1[1])
price1 = float(line1[2])

line2 = input().split()
amount2 = int(line2[1])
price2 = float(line2[2])

print("VALOR A PAGAR: R$ {:.2f}".format(calculateValueToPay(amount1, price1, amount2, price2)))
