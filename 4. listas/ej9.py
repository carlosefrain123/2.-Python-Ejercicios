"""
Tienes el registro de puntos de 4 jugadores
en 3 partidas.

Tu tarea:
1. Imprimir el total de puntos de cada jugador
2. Imprimir el jugador con menor total
3. Imprimir los jugadores que nunca bajaron de 50 puntos
"""

puntos = [
    [40, 45, 40],   # Álvaro
    [60, 70, 55],   # Beatriz
    [90, 85, 95],   # César
    [40, 60, 75],   # Diana
]
jugadores = ["Álvaro", "Beatriz", "César", "Diana"]
partidas = ["Partida 1", "Partida 2", "Partida 3"]
print("1. Imprimir el total de puntos de cada jugador")
for i in range(len(puntos)):
    total=0
    for j in range(len(puntos[i])):
        total+=puntos[i][j]
    print(f"{jugadores[i]}->{total} puntos")
print("2. Imprimir el jugador con menor total")
total_menor = float("inf")
jugador_menor = jugadores[0]

for i in range(len(puntos)):
    total = 0
    for j in range(len(puntos[i])):
        total += puntos[i][j]
    if total < total_menor:
        total_menor = total
        jugador_menor = jugadores[i]

print(f"{jugador_menor} -> {total_menor}")
print("3. Imprimir los jugadores que nunca bajaron de 50 puntos")
for i in range(len(puntos)):
    for j in range(len(puntos[i])):
        if puntos[i][j]>=50:
            print(jugadores[i])
            break