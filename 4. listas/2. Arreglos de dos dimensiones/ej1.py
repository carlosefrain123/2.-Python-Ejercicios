""" Ejercicio 1 → Imprime la nota más alta de María (fila 0) """
notas = [
    [14, 18, 11],   # María
    [10, 13, 16],   # Pedro
    [19, 20, 15],   # Lucía
]
nombres = ["María", "Pedro", "Lucía"]

nota_alta_maria=notas[2][0]
for i in range(len(notas)):
    if notas[2][i]>nota_alta_maria:
        nota_alta_maria=notas[2][i]
print(f'{nombres[0]}, su nota más alta es: {nota_alta_maria}')