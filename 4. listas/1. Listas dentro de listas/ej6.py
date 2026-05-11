""" Ejercicio 2 → Cuenta cuántos elementos tiene cada lista y el total
Resultado:
Lista 0: 4 elementos
Lista 1: 2 elementos
Lista 2: 3 elementos
Total: 9 elementos
"""
inventario = [
    ["manzana", "pera", "uva", "mango"],
    ["leche", "queso"],
    ["arroz", "fideos", "quinua"]
]
for i in range(len(inventario)):
    conteo=0
    for j in range(len(inventario[i])):
        conteo+=1
    print(f'fila: {i}, conteo: {conteo}')