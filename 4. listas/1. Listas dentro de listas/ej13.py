""" Tienes grupos de sobrevivientes organizados
por zona del búnker.
Tu tarea es:
1. Imprimir todos los sobrevivientes con su zona
2. Encontrar la zona con más sobrevivientes
3. Imprimir al líder (primer sobreviviente) de cada zona """
zonas = [
    ["Rick", "Daryl", "Michonne", "Carol"],  # zona norte
    ["Maggie", "Glenn"],                      # zona sur
    ["Negan", "Dwight", "Simon"]             # zona este
]
nombres_zonas = ["Norte", "Sur", "Este"]
print("1. Imprimir todos los sobrevivientes con su zona")
for i in range(len(zonas)):
    for j in range(len(zonas[i])):
        print(f"{nombres_zonas[i]}->{zonas[i][j]}")
print("\n2. Encontrar la zona con más sobrevivientes")
conteo_general=0
for i in range(len(zonas)):
    conteo=0
    mejor_zona=nombres_zonas[0]
    for j in range(len(zonas[i])):
        conteo+=1
    if conteo>conteo_general:
        conteo_general=conteo
        mejor_zona=nombres_zonas[i]
print(f"{mejor_zona}->{conteo_general}")
print("\n3. Imprimir al líder (primer sobreviviente) de cada zona")
for i in range(len(zonas)):
    print(zonas[i][0])