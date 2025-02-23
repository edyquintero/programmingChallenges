point = float(input())

if 0 <= point <= 25:
    print(f"Intervalo [0,25]")
elif 25 <= point <= 50:
    print(f"Intervalo (25,50]")
elif 50 <= point <= 75:
    print(f"Intervalo (50,75]")
elif 75 <= point <= 100:
    print(f"Intervalo (75,100]")
else:
    print(f"Fora de intervalo")