"""
Tienes las notas de 4 estudiantes en 3 materias.
El sistema usa esta escala:
  >= 14 → Aprobado
  < 14  → Desaprobado

Tu tarea:
1. Imprimir cuántas materias aprobó cada estudiante
2. Imprimir la materia con mayor cantidad de aprobados
3. Imprimir los estudiantes que aprobaron TODAS las materias
"""

notas = [
    [15, 16, 16],  # Ana
    [13, 11, 11],  # Bruno
    [16, 18, 19],  # Clara
    [10, 15, 17],  # Diego
]
estudiantes = ["Ana", "Bruno", "Clara", "Diego"]
materias = ["Matemática", "Historia", "Ciencias"]
print("1. Imprimir cuántas materias aprobó cada estudiante")
for i in range(len(notas)):
    cont_notas_alum=0
    cont=0
    for j in range(len(notas[i])):
        if notas[i][j]>=14:
            cont+=1
    print(f"Estudiante {estudiantes[i]}, aprobó: {cont} materias")
print("2. Imprimir la materia con mayor cantidad de aprobados")
for j in range(len(notas[0])):
    cont=0
    for i in range(len(notas)):
        if notas[i][j]>=14:
            cont+=1
    if cont>total_notas:
        total_notas=cont
        materia_mas_nota=materias[j]
print(f"{materia_mas_nota}: {total_notas}")
print("3. Imprimir los estudiantes que aprobaron TODAS las materias")
for i in range(len(notas)):
    conteo=0
    for j in range(len(notas[i])):
        if notas[i][j]>=14:
            conteo+=1
    if conteo==len(materias):
        print(f"Estudiante {estudiantes[i]} -> Cursos aprobados: {conteo}")
            

    

