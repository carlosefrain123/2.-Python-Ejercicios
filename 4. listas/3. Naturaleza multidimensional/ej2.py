""" Ejercicio 2 → Encuentra la posición del tesoro "T" """
mapa = [
    [".", ".", "."],
    [".", ".", "T"],
    [".", ".", "."]
]
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        if mapa[i][j]=="T":
            print(f'T se encuentra en la fila {i} y columna {j}')
            