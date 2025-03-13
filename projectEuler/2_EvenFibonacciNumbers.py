def sum_even_fibonacci(limit):
    a, b = 1, 2
    total = 0
    while b <= limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total

print(sum_even_fibonacci(4000000))
