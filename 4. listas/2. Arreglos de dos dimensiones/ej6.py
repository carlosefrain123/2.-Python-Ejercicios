""" Ejercicio 2 → Encuentra al mejor estudiante de cada materia 

Solución:
Matemática: Lucía con 19
Lenguaje: María con 18
Historia: Pedro con 16
"""
notas = [
    [14, 18, 11],   # María
    [10, 15, 16],   # Pedro
    [19, 12, 15],   # Lucía
]
nombres = ["María", "Pedro", "Lucía"]
materias = ["Matemática", "Lenguaje", "Historia"]


for i in range(len(notas)):
    mayor_nota=notas[0][0]
    for j in range(len(notas[i])):
        if notas[i][j]>mayor_nota:
            mayor_nota=notas[i][j]
    print(f"{materias[i]}: {nombres[i]} con {mayor_nota}")