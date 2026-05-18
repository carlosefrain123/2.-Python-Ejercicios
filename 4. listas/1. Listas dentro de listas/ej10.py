# Cada lista tiene: [vendedor, lunes, martes, miércoles, jueves, viernes]
#darle segunda vuelta
ventas = [
    ["Ana",    150, 200, 180, 220, 190],
    ["Luis",   880, 150, 130, 160, 140],
    ["María",  200, 180, 210, 195, 205]
]
dias_ventas=["vendedor", "lunes", "martes", "miércoles", "jueves", "viernes"]
# Tu tarea:
# 1. Calcula el total vendido por cada vendedor
# 2. Encuentra el mejor día de ventas de cada vendedor
# 3. Encuentra al vendedor con mayor total
venta_grande=0
mejor_vendedor=""
for i in range(len(ventas)):
    mejor_venta=ventas[i][1]
    mejor_dia=dias_ventas[1]
    sum_ventas=0
    for j in range(1,len(ventas[i])):
        sum_ventas+=ventas[i][j]
        if ventas[i][j]>mejor_venta:
            mejor_venta=ventas[i][j]
            mejor_dia=dias_ventas[j]
    print(f"{ventas[i][0]} → total: {sum_ventas}, mejor día: {mejor_dia} ({mejor_venta})")
    if sum_ventas>venta_grande:
        venta_grande=sum_ventas
        mejor_vendedor=ventas[i][0]
print(f"El mejor vendedor es {mejor_vendedor} con {venta_grande}")
    