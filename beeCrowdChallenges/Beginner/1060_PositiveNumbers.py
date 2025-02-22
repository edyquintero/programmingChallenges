numbers = []

for i in range(6):
    num = float(input())
    numbers.append(num)

positive_numbers = 0

for n in numbers:
    if n > 0:
        positive_numbers += 1

print(f"{positive_numbers} valores positivos")