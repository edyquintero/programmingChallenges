count_positive_numbers = 0
sum_positive_numbers = 0

for _ in range(6):
    num = float(input())
    if num > 0:
        count_positive_numbers += 1
        sum_positive_numbers += num

print(f"{count_positive_numbers} valores positivos")
print(f"{sum_positive_numbers / count_positive_numbers:.1f}")
