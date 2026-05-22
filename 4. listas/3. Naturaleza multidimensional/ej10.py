""" Tienes un mapa de un juego con 3 pisos.
Cada piso tiene celdas que pueden contener:
"M" = monstruo
"T" = tesoro
"." = vacío
Tu tarea es:
1. Contar cuántos monstruos hay en total
2. Encontrar todos los tesoros con su ubicación
3. Contar cuántos monstruos hay en cada piso """
mapa = [
    [["M", ".", "T"], [".", "M", "."]],   # piso 0
    [["T", "M", "."], ["M", ".", "M"]],   # piso 1
    [["M", "M", "M"], ["T", "M", "."]]    # piso 2
]
pisos=["piso1","piso2","piso3"]

print("1. Contar cuántos monstruos hay en total")
total=0
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        for k in range(len(mapa[i][j])):
            if mapa[i][j][k]=="M":
                total+=1
print("Hay: ",total,"Mostruos")
print("2. Encontrar todos los tesoros con su ubicación")
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        for k in range(len(mapa[i][j])):
            if mapa[i][j][k] in "T":
                print(f"Piso: {i} | Fila: {j} | Columna {k}")
print("3. Contar cuántos monstruos hay en cada piso")
for i in range(len(mapa)):
    cont=0
    for j in range(len(mapa[i])):
        for k in range(len(mapa[i][j])):
            if mapa[i][j][k]=="M":
                cont+=1
    print(pisos[i],"->",cont,"Mostruos")