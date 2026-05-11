""" Ejercicio 1 → Reemplaza números pares por "P" e impares por "I" 

Resultado:
['I', 'P', 'I']
['P', 'I', 'P']
['I', 'P', 'I']
"""
tablero = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(tablero)):
    for j in range(len(tablero[i])):
        if tablero[i][j]%2==0:
            tablero[i][j]="P"
        else:
            tablero[i][j]="I"
        print(tablero[i][j])