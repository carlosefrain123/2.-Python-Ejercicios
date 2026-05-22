""" Tienes el registro de ventas de 3 vendedores
en 3 meses diferentes.
Tu tarea es:
1. Calcular el total vendido por cada vendedor
2. Calcular el total vendido en cada mes
3. Encontrar al vendedor con mayor total """
ventas = [
    [500, 600, 700],   # Ana
    [900, 400, 800],   # Luis
    [800, 200, 600],   # Rosa
]
nombres = ["Ana", "Luis", "Rosa"]
meses = ["Enero", "Febrero", "Marzo"]

print("1. Calcular el total vendido por cada vendedor")
for i in range(len(ventas)):
    total_vende=0
    for j in range(len(ventas[i])):
        total_vende+=ventas[i][j]
    print(nombres[i],"->",total_vende)
    
print("2. Calcular el total vendido en cada mes")
for j in range(len(ventas[0])):
    total_mes=0
    for i in range(len(ventas)):
        total_mes+=ventas[i][j]
    print(meses[j],"->",total_mes)
print("3. Encontrar al vendedor con mayor total")
max_total_vende=0
for i in range(len(ventas)):
    total_vende=0
    for j in range(len(ventas[i])):
        total_vende+=ventas[i][j]
    if total_vende>max_total_vende:
        max_total_vende=total_vende
        mejor_vendedor=nombres[i]
print(mejor_vendedor,"->",max_total_vende)
        