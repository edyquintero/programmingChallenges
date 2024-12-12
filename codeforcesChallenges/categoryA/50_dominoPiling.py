data = input().split()
M = int(data[0])
N = int(data[1])

def calculateDominos(rows, columns):
    if (rows*columns)%2 != 0:
        return int(((rows*columns)-1)/2)
    else:
        return int((rows*columns)/2)


print(calculateDominos(M, N))