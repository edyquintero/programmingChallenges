def calculateTotalSalary(baseSalary, salesAmount):
    return baseSalary + (salesAmount * 0.15)


name = input()
salary = float(input())
sales = float(input())

print("TOTAL = R$ {:.2f}".format(calculateTotalSalary(salary, sales)))

