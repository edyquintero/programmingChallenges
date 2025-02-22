notes = input().split()

def calculateMedia(data):
    note1 = float(data[0])
    note2 = float(data[1])
    note3 = float(data[2])
    note4 = float(data[3])

    media = (note1*2 + note2*3 + note3*4 + note4*1)/10
    return media

print(f"Media: {calculateMedia(notes):.1f}")
if calculateMedia(notes) >= 7:
    print("Aluno aprovado.")
elif calculateMedia(notes) < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    notaExamen = float(input())
    print(f"Nota do exame: {notaExamen}")
    if (calculateMedia(notes) + notaExamen)/2 >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {(calculateMedia(notes) + notaExamen)/2:.1f}")
