"""
Tienes las temperaturas registradas en 3 ciudades
durante 4 meses.

Tu tarea:
1. Encontrar la ciudad más fría de cada mes
2. Calcular el promedio de temperatura por mes
3. Imprimir el mes con mayor promedio global
"""

temperaturas = [
    [18, 50, 60, 60],  # Lima
    [12, 50, 20, 80],  # Cusco
    [80, 30, 33, 31],  # Piura
]
ciudades = ["Lima", "Cusco", "Piura"]
meses = ["Enero", "Febrero", "Marzo", "Abril"]
print("1. Encontrar la ciudad más fría de cada mes")
for j in range(len(temperaturas[0])):
    temp_alta=temperaturas[0][j]
    ciudad_mas_frio=ciudades[0]
    for i in range(len(temperaturas)):
        """ print(temperaturas[i][j]) """
        if temperaturas[i][j]>temp_alta:
            temp_alta=temperaturas[i][j]
            ciudad_mas_frio=ciudades[i]
    print(f"{meses[j]}->{ciudad_mas_frio}->{temp_alta}")
print("2. Calcular el promedio de temperatura por mes")
for j in range(len(temperaturas[0])):
    total_temp=0
    cont=0
    for i in range(len(temperaturas)):
        total_temp+=temperaturas[i][j]
        cont+=1
    print(f"Mes: {meses[j]} - Promedio: {round(total_temp/cont,2)}")
print("3. Imprimir el mes con mayor promedio global")
promedio_global=0
mes_mayor=meses[0]
for j in range(len(temperaturas[0])):
    total_temp=0
    cont=0
    for i in range(len(temperaturas)):
        total_temp+=temperaturas[i][j]
        cont+=1
    promedio=total_temp/cont
    if promedio>promedio_global:
        promedio_global=promedio
        mes_mayor=meses[j]
print(f"Mes {mes_mayor} -> {round(promedio_global,2)}")
        