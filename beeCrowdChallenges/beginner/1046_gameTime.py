hours = input().split()

start = int(hours[0])
end = int(hours[1])

if start == end:
    print(f"O JOGO DUROU 24 HORA(S)")
elif start > end:
    print(f"O JOGO DUROU {24 -start + end} HORA(S)")
else:
    print(f"O JOGO DUROU {end - start} HORA(S)")