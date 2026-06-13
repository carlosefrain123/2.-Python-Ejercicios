"""
Tienes el registro de faltas de 4 empleados
durante 3 meses.

Tu tarea:
1. Imprimir el empleado con más faltas en total
2. Imprimir el mes con menos faltas en total (suma por columna)
3. Imprimir los empleados que tuvieron al menos un mes con 0 faltas
"""

faltas = [
    [2, 0, 1],   # Ana
    [0, 3, 9],   # Bruno
    [1, 5, 2],   # Clara
    [0, 2, 4],   # Diego
]
empleados = ["Ana", "Bruno", "Clara", "Diego"]
meses = ["Enero", "Febrero", "Marzo"]
print("1. Imprimir el empleado con más faltas en total")
gen_sum_empl=0
for i in range(len(faltas)):
    sum_empl=0
    for j in range(len(faltas[i])):
        sum_empl+=faltas[i][j]
    if sum_empl>gen_sum_empl:
        gen_sum_empl=sum_empl
        empl_mas_falta=empleados[i]
print(f"Empleado con más faltas: {empl_mas_falta} - Faltas: {gen_sum_empl}")
print("2. Imprimir el mes con menos faltas en total (suma por columna)")
totales_mes=[]
for j in range(len(faltas[0])):
    total_mes=0
    for i in range(len(faltas)):
        total_mes+=faltas[i][j]
    totales_mes.append(total_mes)
    print(f"Total faltas en {meses[j]}: {total_mes}")
print("3. Imprimir los empleados que tuvieron al menos un mes con 0 faltas")
for i in range(len(faltas)):
    for j in range(len(faltas[i])):
        if faltas[i][j]==0:
            empleados_con_cero=empleados[i]
            print(empleados_con_cero)
    