""" Caso 1 → Encuentra al estudiante con mayor promedio general """
notas = [
    [12, 15, 18],   # Rosa
    [20, 14, 16],   # Juan
    [11, 19, 13],   # Diego
]
nombres = ["Rosa", "Juan", "Diego"]
max_promedio=0
mejor_estudiante=""
for i in range(len(notas)):
    total=0
    for j in range(len(notas[i])):
        total+=notas[i][j]
    promedio=total/len(notas[i])
    if promedio>max_promedio:
        max_promedio=promedio
        mejor_estudiante=nombres[i]
print(mejor_estudiante,"->",max_promedio)