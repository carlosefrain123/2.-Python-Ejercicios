"""
Caso → Encuentra al estudiante con 
mayor nota en cada materia
 """
notas = [
    #C   J   R
    [15, 12, 18],   # M
    [12, 16, 14],   # L
    [19, 11, 16],   # H
    [11, 20, 12],   # A
    
]
nombres = ["Carmen", "Jorge", "Rosa"]
materias = ["Matemática", "Lenguaje", "Historia","Anatomia"]
for i in range(len(notas)):
    mejor_nota=notas[i][0]
    mejor_alumno=nombres[0]
    for j in range(len(notas[i])):
        if notas[i][j]>mejor_nota:
            mejor_nota=notas[i][j]
            mejor_alumno=nombres[j]
    print(f"{materias[i]}: {mejor_alumno}->{mejor_nota}")
    