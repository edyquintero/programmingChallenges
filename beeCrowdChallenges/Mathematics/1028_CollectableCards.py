def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
for _ in range(n):
    f1, f2 = map(int, input().split())
    print(gcd(f1, f2))
