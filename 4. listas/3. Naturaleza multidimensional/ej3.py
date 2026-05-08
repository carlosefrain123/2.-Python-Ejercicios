""" Ejercicio 3 → Cambia todos los "X" por "O" """
tablero = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
]
for i in range(len(tablero)):
    for j in range(len(tablero[i])):
        if tablero[i][j]=="X":
            tablero[i][j]="O"
        print(tablero[i][j])