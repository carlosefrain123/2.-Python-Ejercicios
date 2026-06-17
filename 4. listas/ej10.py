"""
Tienes las horas trabajadas de 3 técnicos
en 4 semanas.

Tu tarea:
1. Imprimir el total de horas por semana
2. Imprimir la semana con menos horas en total
3. Imprimir los técnicos que trabajaron más de 35 horas
   en al menos una semana
"""

horas = [
    [30, 20, 18, 25],   # Renzo
    [35, 12, 30, 36],   # Paola
    [28, 38, 42, 33],   # Luis
]
tecnicos = ["Renzo", "Paola", "Luis"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]
print("1. Imprimir el total de horas por semana")
for j in range(len(horas[0])):
    total_horas=0
    for i in range(len(horas)):
        total_horas+=horas[i][j]
    print(f"{semanas[j]}->{total_horas}")
print("2. Imprimir la semana con menos horas en total")
total_menor=float("inf")
semana_menor=semanas[0]
for j in range(len(horas[0])):
    total_horas=0
    for i in range(len(horas)):
        total_horas+=horas[i][j]
    if total_horas<total_menor:
        total_menor=total_horas
        semana_menor=semanas[j]
print(f"{semana_menor}->{total_menor}")
print("3. Imprimir los técnicos que trabajaron más de 35 horas en al menos una semana")
for i in range(len(horas)):
    for j in range(len(horas[i])):
        if horas[i][j]>35:
            print(tecnicos[i])
            break