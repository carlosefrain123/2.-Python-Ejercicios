# Cada lista representa un equipo con sus puntajes por ronda
equipos = [
    ["Equipo A", 85, 92, 78, 95],
    ["Equipo B", 80, 70, 91, 98],
    ["Equipo C", 99, 90, 82, 90]
]

# Tu tarea:
# 1. Imprime el nombre de cada equipo
# 2. Calcula su promedio de puntajes
# 3. Encuentra al equipo ganador

""" print("1. Imprime el nombre de cada equipo")
for i in range(len(equipos)):
    print(equipos[i][0]) """
print("2. Calcula su promedio de puntajes")
max_promedio=0
for i in range(len(equipos)):
    sum_notas=0
    cont=0
    for j in range(1,len(equipos[i])):
        """ print(equipos[i][j]) """
        sum_notas+=equipos[i][j]
        cont+=1
    promedio=round(sum_notas/cont,2)
    #Calcula el quipo ganador:
    if promedio>max_promedio:
        max_promedio=promedio
        equipo_ganador=equipos[i][0]
    """ print(f"{equipos[i][0]}, suma de notas: {sum_notas}") """
    print(f"{equipos[i][0]}, promedio: {promedio}")
print(f"Máximo promedio: {max_promedio}")
print(f"Equipo ganador: {equipo_ganador}")

    