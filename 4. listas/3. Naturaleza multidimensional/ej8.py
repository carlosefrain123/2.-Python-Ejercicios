""" Caso 2 → Encuentra el número más grande de todo el cubo """
cubo = [
    [[3, 7], [1, 9]],
    [[15, 2], [6, 4]],
    [[8, 111], [5, 20]]
]
mayor_numero=cubo[0][0][0]
for i in range(len(cubo)):
    for j in range(len(cubo[i])):
        for k in range(len(cubo[i][j])):
            if cubo[i][j][k]>mayor_numero:
                mayor_numero=cubo[i][j][k]
print(mayor_numero)