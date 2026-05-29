""" Tienes un mapa 3D del búnker con 3 pisos.
Cada celda puede contener:
"Z" = zombie
"S" = sobreviviente
"." = vacío
Tu tarea es:
1. Contar cuántos zombies hay en total
2. Encontrar todos los sobrevivientes con su ubicación
3. Contar zombies por piso """
bunker = [
    [["Z", ".", "S"], [".", "Z", "."]],   # piso 0
    [["S", "Z", "."], ["Z", ".", "S"]],   # piso 1
    [[".", "Z", "Z"], ["S", "Z", "."]]    # piso 2
]
print("1. Contar cuántos zombies hay en total")
count=0
for i in range(len(bunker)):    
    for j in range(len(bunker[i])):
        for k in range(len(bunker[i][j])):
            if bunker[i][j][k]=="Z":
                count+=1
print(count)
print("\n2. Encontrar todos los sobrevivientes con su ubicación")
count=0
for i in range(len(bunker)):    
    for j in range(len(bunker[i])):
        for k in range(len(bunker[i][j])):
            if bunker[i][j][k]== "S":
                count+=1
print(count)
print("\n 3. Contar zombies por piso")
for i in range(len(bunker)):    
    count=0
    for j in range(len(bunker[i])):
        for k in range(len(bunker[i][j])):
            if bunker[i][j][k]=="Z":
                count+=1
    print(count)