""" Estás coordinando los equipos de defensa del búnker.
Cada lista contiene: [nombre_lider, *miembros, *armas]
donde los primeros datos son personas y los últimos son armas.

equipos = [
    ["Rick",     "Daryl", "Glenn",    "AK-47", "Pistola", "Ballesta"],
    ["Michonne", "Carol", "Maggie",   "Katana", "Escopeta", "Granada"],
    ["Negan",    "Dwight","Simon","Lucille", "AK-47", "Pistola", "Mina"]
]
personas = 3  # los primeros 3 elementos son personas
armas    = 3  # los últimos 3 elementos son armas (excepto equipo 3 que tiene 4)

Tu tarea es:
1. Imprimir líder, miembros y armas de cada equipo por separado
2. Contar el total de personas y armas en el búnker
3. Encontrar al equipo con más armas
4. Verificar si el arma "AK-47" está en más de un equipo
   y mostrar en cuáles """
equipos = [
    ["Rick",     "Daryl", "Glenn",    "AK-47", "Pistola", "Ballesta"],
    ["Michonne", "Carol", "Maggie",   "Katana", "Escopeta", "Granada"],
    ["Negan",    "Dwight","Simon","Lucille", "AK-47", "Pistola", "Mina"]
]
personas = 3  # los primeros 3 elementos son personas
armas    = 3  # los últimos 3 elementos son armas (excepto equipo 3 que tiene 4)
print("1. Imprimir líder, miembros y armas de cada equipo por separado")
for i in range(len(equipos)):
        print(equipos[i][0])
print("2. Contar el total de personas y armas en el búnker")
total_personas=0
total_armas=0
for i in equipos:
    total_personas+=3
    total_armas=len(i)-3
print("Total personas:", total_personas)  # 9
print("Total armas:", total_armas)        # 3 + 3 + 4 = 10
print("3. Encontrar al equipo con más armas")
max_total_armas=0
equipo_mas_armas = None
for i in equipos:
    total_armas=len(i)-3
    if total_armas>max_total_armas:
        max_total_armas=total_armas
        equipo_mas_armas = i
print("Equipo con más armas:", equipo_mas_armas)
print("Cantidad de armas:", max_total_armas)
print("Verificar si el arma AK-47 está en más de un equipo y mostrar en cuáles")
print("Verificar si el arma AK-47 está en más de un equipo y mostrar en cuáles")

# Lista para guardar los equipos que tienen AK-47
equipos_con_ak47 = []

# Recorrer cada equipo con su índice
for i in range(len(equipos)):
    # Verificar si "AK-47" está en el equipo actual
    if "AK-47" in equipos[i]:
        equipos_con_ak47.append(i)  # Guardar el índice del equipo

# Verificar resultado
if len(equipos_con_ak47) > 1:
    print(f"AK-47 está en {len(equipos_con_ak47)} equipos")
    print("Equipos:", equipos_con_ak47)
    
    # Mostrar nombres de los líderes de esos equipos
    for indice in equipos_con_ak47:
        print(f"  - Equipo {indice}: {equipos[indice][0]}")
else:
    print("AK-47 está en menos de 2 equipos")