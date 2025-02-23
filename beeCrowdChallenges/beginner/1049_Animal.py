in1 = input()
in2 = input()
in3 = input()

if in1 == "vertebrado":
    if in2 == "ave":
        if in3 == "carnivoro":
            print("aguia")
        if in3 == "onivoro":
            print("pomba")
    if in2 == "mamifero":
        if in3 == "onivoro":
            print("homem")
        if in3 == "herbivoro":
            print("vaca")
if in1 == "invertebrado":
    if in2 == "inseto":
        if in2 == "hematofago":
            print("pulga")
        if in3 == "herbivoro":
            print("lagarta")
    if in2 == "anelideo":
        if in3 == "hematofago":
            print("sanguessuga")
        if in3 == "onivoro":
            print("minhoca")
