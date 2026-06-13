"""
Tienes el inventario de 4 tiendas.
Cada fila es una tienda, cada columna es un producto.

Tu tarea:
1. Imprimir el stock total de cada tienda
2. Imprimir el producto con menor stock en cada tienda
3. Imprimir la tienda que tiene el mayor stock total
"""

stock = [
    [120, 45, 200, 80],   # Tienda A
    [60,  90, 150, 30],   # Tienda B
    [5, 10,  80, 95],   # Tienda C
    [75, 130,  60, 110],  # Tienda D
]
tiendas = ["Tienda A", "Tienda B", "Tienda C", "Tienda D"]
productos = ["Arroz", "Aceite", "Harina", "Azúcar"]
print("1. Imprimir el stock total de cada tienda")
for i in range(len(stock)):
    total=0
    for j in range(len(stock[i])):
        total+=stock[i][j]
    print(f"La tienda {tiendas[i]} -> {total}")
print("2. Imprimir el producto con menor stock en cada tienda")
for i in range(len (stock)):
    menor_stock=stock[i][0]
    for j in range(len(stock[i])):
        if stock[i][j]<menor_stock:
            menor_stock=stock[i][j]
            pro_stock_menor=productos[j]
    print(f"{pro_stock_menor} -> {menor_stock}")
print("3. Imprimir la tienda que tiene el mayor stock total")
stock_total=0
for i in range(len(stock)):
    total=0
    mayor_tienda=tiendas[0]
    for j in range(len(stock[i])):
        total+=stock[i][j]
    if total>stock_total:
        stock_total=total
        mayor_tienda=tiendas[i]
print(f"{mayor_tienda} -> {stock_total}")