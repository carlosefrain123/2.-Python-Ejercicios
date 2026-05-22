""" Tienes un almacén con 3 pisos, cada piso tiene
2 estantes y cada estante tiene 3 productos.
Tu tarea es:
1. Contar el total de productos
2. Buscar si existe el producto "Leche"
3. Listar todos los productos del piso 1 """
almacen = [
    [["Pan", "Agua", "Leche"],   ["Arroz", "Azúcar", "Sal"]],
    [["Shampoo", "Jabón", "Crema"], ["Escoba", "Trapeador", "Balde"]],
    [["Polo", "Pantalón", "Zapatos"], ["Gorra", "Bufanda", "Guantes"]]
]
pisos=["piso1","piso2","piso3"]

print("1. Contar el total de productos")
total=0
for i in range(len(almacen)):
    for j in range(len(almacen[i])):
        for k in range(len(almacen[i][j])):
            total+=1
print("Total de porductos: ",total)
print("2. Buscar si existe el producto 'Leche'")
encontrado = False
for i in range(len(almacen)):
    for j in range(len(almacen[i])):
        for k in range(len(almacen[i][j])):
            if almacen[i][j][k] == "Leche":
                encontrado = True
                break
if encontrado:
    print("Existe el producto Leche")
else:
    print("No existe el producto Leche")
print("3. Listar todos los productos del piso 1")
for j in range(len(almacen[0])):
    for k in range(len(almacen[0][j])):
        print(pisos[0],"->",{almacen[0][j][k]})
