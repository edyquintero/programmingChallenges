"""The prime factors of 13195 are 5, 7, 13 and 29
What is the largest prime factor of the number 600851475143"""
def largest_prime_factor(n):
    factor = 2
    while n % factor == 0:
        n //= factor

    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 2

    return n if n > 1 else factor

print(largest_prime_factor(600851475143))
