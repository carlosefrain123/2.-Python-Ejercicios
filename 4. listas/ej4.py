"""
Tienes las horas de estudio de 4 estudiantes
durante 3 semanas.

Tu tarea:
1. Calcular el promedio de horas por semana (todas las semanas)
2. Encontrar al estudiante que más estudió en cada semana
3. Imprimir la semana con mayor promedio global
"""

horas = [
    [12, 10, 10],  # Ana
    [20,  10, 14],  # Bruno
    [19, 12, 35],  # Clara
    [18, 13, 10],  # Diego
]
estudiantes = ["Ana", "Bruno", "Clara", "Diego"]
semanas = ["Semana 1", "Semana 2", "Semana 3"]
print("1. Calcular el promedio de horas por semana (todas las semanas)")
for j in range(len(horas[0])):
    totalXsemana=0
    conteo=0
    for i in range(len(horas)):
        totalXsemana+=horas[i][j]
        conteo+=1
    promedio=round(totalXsemana/conteo,2)
    print(f"{semanas[j]}->{promedio}")
print("2. Encontrar al estudiante que más estudió en cada semana")
horas_mas_estudio=0
for j in range(len(horas[0])):
    for i in range(len(horas)):
        if horas[i][j]>horas_mas_estudio:
            horas_mas_estudio=horas[i][j]
            semana_mayor=semanas[j]
print(f"{semana_mayor}->{horas_mas_estudio}")
print("3. Imprimir la semana con mayor promedio global")
mayor_promedio=0
for j in range(len(horas[0])):
    totalXsemana=0
    conteo=0
    for i in range(len(horas)):
        totalXsemana+=horas[i][j]
        conteo+=1
    promedio=round(totalXsemana/conteo,2)
    if promedio>mayor_promedio:
        mayor_promedio=promedio
        semana_mayor=semanas[j]
print(f"{semana_mayor}->{mayor_promedio}")
