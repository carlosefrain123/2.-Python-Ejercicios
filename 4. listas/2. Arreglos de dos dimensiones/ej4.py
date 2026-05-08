""" Ejercicio 4 → Encuentra al estudiante con nota más baja en tercera materia """
notas = [
    [14, 18, 11],   # María
    [10, 13, 10],   # Pedro
    [19, 12, 15],   # Lucía
]
nombres = ["María", "Pedro", "Lucía"]

nota_baja=notas[0][2]
peor_estudiante=nombres[0]
for i in range(len(notas)):
    if notas[i][2]<nota_baja:
        nota_baja=notas[i][2]
        peor_estudiante=nombres[i]
print(f'{peor_estudiante} tiene {nota_baja}')