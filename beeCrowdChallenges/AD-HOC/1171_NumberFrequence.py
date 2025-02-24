n = int(input())

numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for num in sorted(frequency.keys()):
    print(f"{num} aparece {frequency[num]} vez(es)")
