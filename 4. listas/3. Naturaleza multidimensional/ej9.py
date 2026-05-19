edificio = [
    [[2, 3], [4, 5]],
    [[6, 10], [8, 9]],
    [[1, 2], [7, 9]]
]
piso_edificio=["piso A","piso B","piso C"]
for i in range(len(edificio)):
    conteo=0
    for j in range(len(edificio[i])):
        for k in range(len(edificio[i][j])):
            """ print(edificio[i][j][k]) """
            if edificio[i][j][k]%2==0:
                conteo+=1
                """ print(edificio[i][j][k]) """
    print(f"{piso_edificio[i]}, tiene {conteo} pares")