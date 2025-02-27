test_cases = int(input())

for i in range(test_cases):
    available_food = float(input())
    days = 0

    while available_food > 1.0:
        available_food /= 2
        days += 1

    print(f"{days} dias")
