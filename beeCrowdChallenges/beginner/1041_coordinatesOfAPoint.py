coordinates = input().split()

x = float(coordinates[0])
y = float(coordinates[1])

def calculateQuadrant(posx, posy):
    if posx == 0 and posy == 0:
        print("Origem")
    elif posx == 0 and posy != 0:
        print("Eixo Y")
    elif posy == 0 and posx != 0:
        print("Eixo X")
    elif posy > 0 and posx > 0:
        print("Q1")
    elif posy > 0 > posx:
        print("Q2")
    elif posy < 0 > posx:
        print("Q3")
    else:
        print("Q4")


calculateQuadrant(x,y)