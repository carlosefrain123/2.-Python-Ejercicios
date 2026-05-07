""" Ejercicio 2 → Suma todas las notas de Pedro (fila 1) """
notas = [
    [14, 18, 11],   # María
    [10, 13, 16],   # Pedro
    [19, 12, 15],   # Lucía
]
nombres = ["María", "Pedro", "Lucía"]

total=0
for i in range(len(notas)):
    total+=notas[1][i]
print(f'La suma de {nombres[1]} es: {total}')