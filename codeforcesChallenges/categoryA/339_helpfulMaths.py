def sort_sum(sum):
    numbers = sum.split('+')
    numbers.sort()
    return '+'.join(numbers)

sum = input().strip()

print(sort_sum(sum))