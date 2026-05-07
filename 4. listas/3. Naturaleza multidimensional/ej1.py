""" Ejercicio 1 → Cuenta cuántas estrellas "E" hay """
mapa = [
    [".", "E", "."],
    ["E", ".", "."],
    [".", ".", "E"]
]
conteo=0
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        if mapa[i][j]=="E":
            """ print(mapa[i][j]) """
            conteo+=1
print(f'Hay {conteo} E')
        