""" Ejercicio 1 → Calcula el promedio de cada estudiante y clasifica

Solución:
María: 14.3 → Aprobado ✅
Pedro: 13.0 → Desaprobado ❌
Lucía: 15.3 → Aprobado ✅
"""
notas = [
    [14, 18, 11],   # María
    [10, 13, 16],   # Pedro
    [19, 12, 15],   # Lucía
]
nombres = ["María", "Pedro", "Lucía"]

for i in range(len(notas)):
    total=0
    conteo=0
    for j in range(len(notas[i])):
        total+=notas[i][j]
        conteo+=1
    promedio=total/conteo
    print(f'{nombres[i]}, tiene un promedio de: {round(promedio,1)}')