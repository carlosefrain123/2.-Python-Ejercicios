"""
Tienes las ventas de 3 vendedores en 4 regiones.

Tu tarea:
1. Imprimir el total vendido por cada vendedor (suma su fila)
2. Imprimir la región con mayor venta total (suma por columna)
3. Encontrar la celda con la venta más alta 
   e imprimir: vendedor, región y monto
"""

ventas = [
    [910, 900, 300, 800],   # Carlos
    [800, 200, 960, 400],   # Lucia
    [350, 600, 950, 500],   # Pedro
]
vendedores = ["Carlos", "Lucia", "Pedro"]
regiones = ["Norte", "Sur", "Este", "Oeste"]

print("1. Imprimir el total vendido por cada vendedor (suma su fila)")
for i in range(len(ventas)):
    total_vendedor=0
    for j in range(len(ventas[i])):
        total_vendedor+=ventas[i][j]
    print(f"{vendedores[i]}->{total_vendedor}")
print("2. Imprimir la región con mayor venta total (suma por columna)")
for j in range(len(ventas[0])):
    total=0
    for i in range(len(ventas)):
        total+=ventas[i][j]
    print(f"{regiones[j]}->{total}")
print("3. Encontrar la celda con la venta más alta ")
venta_general=0
for j in range(len(ventas[0])):
    for i in range(len(ventas)):
        if ventas[i][j]>venta_general:
            venta_general=ventas[i][j]
            vende_max=vendedores[i]
            reg_max=regiones[j]
print(f"Vendedor Max: {vende_max} - Region máximo: {reg_max} - Venta Max: {venta_general}")