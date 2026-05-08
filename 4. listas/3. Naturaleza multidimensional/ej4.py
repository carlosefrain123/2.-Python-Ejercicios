""" Ejercicio 4 → Cuenta jugadores "J" por fila """
campo = [
    ["J", ".", "J"],
    [".", "J", "."],
    ["J", "J", "J"]
]
for i in range(len(campo)):
    conteo=0
    for j in range(len(campo[i])):
        if campo[i][j]=="J":
            conteo+=1
    print(f'La fila {i}, tiene {conteo} J')