# 1=presente, 0=ausente
# filas=estudiantes, columnas=días
asistencia = [
    [1, 1, 0, 1, 1],   # Ana
    [1, 0, 0, 1, 0],   # Luis
    [1, 1, 1, 1, 1],   # María
    [0, 1, 1, 0, 1],   # Pedro
]
nombres = ["Ana", "Luis", "María", "Pedro"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Tu tarea:
# 1. Calcula el porcentaje de asistencia de cada estudiante X
# 2. Encuentra qué día tuvo más ausencias 
# 3. Clasifica: >= 80% "Regular" < 80% "Irregular"

# Tareas 1 y 3
for i in range(len(asistencia)):
    sum_asistencia = 0
    conteo = 0
    for j in range(len(asistencia[i])):
        conteo += 1
        if asistencia[i][j] == 1:
            sum_asistencia += 1

    porcentaje = (sum_asistencia / conteo) * 100

    if porcentaje >= 80:
        clasificacion = "Regular"
    else:
        clasificacion = "Irregular"

    print(f"{nombres[i]}: {porcentaje}% → {clasificacion}")

# Tarea 2
print()
max_ausencias = 0
peor_dia = ""

for j in range(len(asistencia[0])):
    ausencias = 0
    for i in range(len(asistencia)):
        if asistencia[i][j] == 0:
            ausencias += 1
    if ausencias > max_ausencias:
        max_ausencias = ausencias
        peor_dia = dias[j]

print(f"El día con más ausencias fue {peor_dia} con {max_ausencias} ausencias")