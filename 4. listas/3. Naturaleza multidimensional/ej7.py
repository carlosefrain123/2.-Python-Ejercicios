""" Caso 1 → Cuenta cuántos números son mayores a 5 en cada piso """
edificio = [
    [[3, 8], [6, 2]],
    [[1, 4], [9, 7]],
    [[5, 6], [3, 8]]
]
conteo=0
for i in range(len(edificio)):
    for j in range(len(edificio[i])):
        for k in range(len(edificio[i][j])):
            """ print(edificio[i][j][k]) """
            if edificio[i][j][k]>5:
                """ print(edificio[i][j][k]) """
                conteo+=1
print(f"Hay {conteo} número mayores a 5")