import sys
import math

for line in sys.stdin:
    try:
        m, n = map(int, line.split())
        print(math.factorial(m) + math.factorial(n))
    except EOFError:
        break
