def decomposeDays(daysToDecompose):
    years = daysToDecompose // 365
    months = (daysToDecompose % 365) // 30
    days = (daysToDecompose % 365) % 30
    return "{} ano(s)\n{} mes(es)\n{} dia(s)".format(years, months, days)


dayComplete = int(input())
print(decomposeDays(dayComplete))
