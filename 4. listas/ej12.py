"""
La fila 0 contiene los nombres de los meses.
Las filas 1 en adelante son los datos de ventas por vendedor.

Tu tarea:
1. Imprimir el total vendido por cada vendedor (filas 1+)
2. Imprimir el mes con mayor venta total (columnas, saltando fila 0)
3. Encontrar al vendedor con mayor venta en un solo mes
"""

tabla = [
    ["Enero", "Febrero", "Marzo", "Abril"],   # fila 0: encabezados
    [500, 800, 650, 720],                      # vendedor Carlos
    [900, 400, 750, 600],                      # vendedor Lucia
    [300, 600, 880, 450],                      # vendedor Pedro
]
vendedores = ["Carlos", "Lucia", "Pedro"]
print("1. Imprimir el total vendido por cada vendedor (filas 1+)")
for i in range(1,len(tabla)):
    total=0
    for j in range(len(tabla[i])):
        total+=tabla[i][j]
    print(f"{vendedores[i-1]}->{total}")
print("2. Imprimir el mes con mayor venta total (columnas, saltando fila 0)")
for j in range(len(tabla[0])):
    total=0
    for i in range(1,len(tabla)):
        total+=tabla[i][j]
    print(f"{tabla[0][j]}->{total}")
print("3. Encontrar al vendedor con mayor venta en un solo mes")
print("3. Encontrar al vendedor con mayor venta en un solo mes")
venta_mayor = float('-inf')
vendedor_mayor = ""
mes_mayor = ""

for i in range(1, len(tabla)):          # salta fila 0 (encabezados)
    for j in range(len(tabla[i])):      # recorre todos los meses
        if tabla[i][j] > venta_mayor:
            venta_mayor = tabla[i][j]
            vendedor_mayor = vendedores[i-1]  # i-1 porque vendedores empieza en 0
            mes_mayor = tabla[0][j]           # el mes está en la fila 0

print(f"{vendedor_mayor} -> {mes_mayor} -> {venta_mayor}")