""" Ejercicio 3 → Imprime nombre y primera nota de cada estudiante """
notas = [
    [14, 18, 11],   # María
    [10, 13, 16],   # Pedro
    [19, 12, 15],   # Lucía
]
nombres = ["María", "Pedro", "Lucía"]

for i in range(len(notas)):
    print(f'La nota de {nombres[i]} es: {notas[i][0]}')