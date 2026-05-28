""" Tienes el registro de zombies eliminados por
cada sobreviviente durante 3 días de defensa.
Tu tarea es:
1. Calcular el total de zombies eliminados por cada uno
2. Calcular el total eliminado cada día
3. Encontrar al sobreviviente más efectivo """
eliminados = [
    [15, 20, 18],   # Rick
    [25, 30, 22],   # Daryl
    [10, 15, 12],   # Michonne
]
nombres = ["Rick", "Daryl", "Michonne"]
dias = ["Día 1", "Día 2", "Día 3"]
print("1. Calcular el total de zombies eliminados por cada uno")
for i in range(len(eliminados)):
    total=0
    for j in range(len(eliminados[i])):
        total+=eliminados[i][j]
    print(f"{nombres[i]} -> {total}")
print("2. Calcular el total eliminado cada día")
for i in range(len(eliminados)):
    total=0
    for j in range(len(eliminados[i])):
        total+=eliminados[i][j]
    print(f"{dias[i]} -> {total}")
print("3. Encontrar al sobreviviente más efectivo")
total_general=0
for i in range(len(eliminados)):
    total=0
    for j in range(len(eliminados[i])):
        total+=eliminados[i][j]
    if total>total_general:
        total_general=total
        mej_sob=nombres[i]
print(f"{mej_sob}->{total_general}")
    