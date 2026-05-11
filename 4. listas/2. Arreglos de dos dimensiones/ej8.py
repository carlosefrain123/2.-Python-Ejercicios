""" Caso 2 → Cuenta cuántos estudiantes aprobaron cada materia (nota >= 11) """
notas = [
    [12, 8,  10],   # Rosa
    [10, 14, 16],   # Juan
    [11, 19, 9],    # Diego
]
materias = ["Matemática", "Lenguaje", "Historia"]
conteo=0
for i in range(len(notas)):
    total=0
    for j in range(len(notas[i])):
        total+=notas[i][j]
    promedio=total/len(notas[i])
    if promedio>11:
        conteo+=1
print(f"Aprobaron más de 11, {conteo} estudiantes")