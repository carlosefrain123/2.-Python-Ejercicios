"""
Cada fila contiene: [nombre_jugador, puntos_ronda1,
                     puntos_ronda2, puntos_ronda3]
La col 0 es el nombre — los datos numéricos empiezan en col 1.

Tu tarea:
1. Imprimir el total de puntos de cada jugador
2. Imprimir la ronda con mayor puntaje de cada jugador
3. Encontrar al jugador con el mayor puntaje en una sola ronda
"""

jugadores = [
    ["Álvaro", 85, 90, 78],
    ["Beatriz", 70, 98, 88],
    ["César",   95, 80, 91],
]
rondas = ["Ronda 1", "Ronda 2", "Ronda 3"]
print("1. Imprimir el total de puntos de cada jugador")
for i in range(len(jugadores)):
    total=0
    for j in range(1,len(jugadores[i])):
        total+=jugadores[i][j]
    print(f"{jugadores[i][0]}->{total}")
print("2. Imprimir la ronda con mayor puntaje de cada jugador")
for i in range(len(jugadores)):
    total_menor=jugadores[i][1]
    for j in range(1,len(jugadores[i])):
        if jugadores[i][j]>total_menor:
            total_menor=jugadores[i][j]
    print(f"{jugadores[i][0]}->{total_menor}")
print("3. Encontrar al jugador con el mayor puntaje en una sola ronda")
puntaje_mayor = float('-inf')  # fuera del for i
jugador_mayor = ""
ronda_mayor = ""
for i in range(len(jugadores)):
    for j in range(1, len(jugadores[i])):
        if jugadores[i][j] > puntaje_mayor:
            puntaje_mayor = jugadores[i][j]
            jugador_mayor = jugadores[i][0]
            ronda_mayor = rondas[j-1]
print(f"{jugador_mayor} -> {ronda_mayor} -> {puntaje_mayor}")  # fuera de todo