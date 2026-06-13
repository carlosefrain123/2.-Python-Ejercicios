"""
Tienes el registro de calorías consumidas por 3 atletas
durante 4 días de entrenamiento.

Tu tarea:
1. Imprimir el total de calorías de cada atleta
2. Imprimir el día donde cada atleta consumió menos calorías
3. Encontrar al atleta con el mayor consumo total
"""
calorias = [
    [2800, 9000, 5000, 3200],  # Sofía
    [1000, 2000, 3800, 2900],  # Miguel
    [2500, 2700, 3100, 2800],  # Valeria
]
nombres = ["Sofía", "Miguel", "Valeria"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves"]
print("1. Imprimir el total de calorías de cada atleta")
for i in range(len(calorias)):
    total_cal=0
    for j in range(len(calorias[i])):
        total_cal+=calorias[i][j]
    print(f"{nombres[i]}->{total_cal}")
print("3. Encontrar al atleta con el mayor consumo total")
num_mayor=0
atl_win=0
for i in range(len(calorias)):
    tca=0
    for j in range(len(calorias[i])):
        tca+=calorias[i][j]
    if tca>num_mayor:
        num_mayor=tca
        atl_win=i
print(f"{nombres[atl_win]}->{num_mayor}")
print("2. Imprimir el día donde cada atleta consumió menos calorías")
for i in range(len(calorias)):
    cal_min = calorias[i][0]   # reinicia por atleta
    dia_min = dias[0]
    for j in range(len(calorias[i])):
        if calorias[i][j] < cal_min:
            cal_min = calorias[i][j]
            dia_min = dias[j]
    print(f"{nombres[i]} -> {dia_min} -> {cal_min}")  # fuera del for interno