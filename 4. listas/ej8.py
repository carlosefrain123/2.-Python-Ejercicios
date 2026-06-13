"""
Tienes el registro de temperatura de 3 almacenes
durante 4 días. El rango seguro es entre 15 y 25 grados.

Tu tarea:
1. Imprimir los días donde cada almacén estuvo fuera del rango
2. Imprimir el almacén con más días fuera del rango
3. Imprimir si hubo algún día donde TODOS los almacenes
   estuvieron dentro del rango al mismo tiempo
"""

temps = [
    [18, 27, 28, 22],  # Almacén A
    [20, 24, 18, 30],  # Almacén B
    [12, 30, 30, 20],  # Almacén C
]
almacenes = ["Almacén A", "Almacén B", "Almacén C"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves"]
print("1. Imprimir los días donde cada almacén estuvo fuera del rango")
for i in range(len(temps)):
    for j in range(len(temps[i])):
        if temps[i][j]<15 or temps[i][j]>25:
            print(f"{almacenes[i]} -> {dias[j]} -> {temps[i][j]}°")
print("2. Imprimir el almacén con más días fuera del rango")
dias_max=0
for i in range(len(temps)):
    cont=0
    for j in range(len(temps[i])):
        if temps[i][j]<15 or temps[i][j]>25:
            cont+=1
    if cont>dias_max:
        dias_max=cont
        almacen_max=almacenes[i]        
print(f"{almacen_max}->{dias_max}")
print("3. Imprimir si hubo algún día donde TODOS los almacenes estuvieron dentro del rango al mismo tiempo")
for j in range(len(temps[0])):
    cont=0
    for i in range(len(temps)):
        if 15<=temps[i][j]<=25:
            cont+=1
    if cont==3:
        print(f"Almenes que estuvieron dentro del rango: {cont}")
