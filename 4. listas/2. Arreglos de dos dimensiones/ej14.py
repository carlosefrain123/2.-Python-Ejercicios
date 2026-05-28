""" Tienes el nivel de infección de 3 zonas del búnker
medido durante 4 días.
Tu tarea es:
1. Calcular el promedio de infección de cada zona
2. Encontrar el día más peligroso de cada zona
3. Clasificar cada zona:
   promedio >= 70 → "Zona roja ☠️ Evacuar"
   promedio >= 40 → "Zona naranja ⚠️ Precaución"
   promedio <  40 → "Zona verde ✅ Segura" """
infeccion = [
    [80, 75, 85, 90],   # zona A
    [30, 35, 40, 25],   # zona B
    [50, 80, 55, 65],   # zona C
]
zonas = ["Zona A", "Zona B", "Zona C"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves"]
print("1. Calcular el promedio de infección de cada zona")
for i in range(len(infeccion)):
    suma=0
    conteo=0
    for j in range(len(infeccion[i])):
        suma+=infeccion[i][j]
        conteo+=1
    promedio=suma/conteo
    print(f"{zonas[i]}->{promedio}")
print("\n2. Encontrar el día más peligroso de cada zona")
for i in range(len(infeccion)):
    dia_peligroso=infeccion[i][0]
    for j in range(len(infeccion[i])):
        if infeccion[i][j]>dia_peligroso:
            dia_peligroso=infeccion[i][j]  
            dia_mayor=dias[j]   
    print(f"{dia_mayor}->{dia_peligroso}")
print("\n3. Clasificar cada zona")
mensaje=""
for i in range(len(infeccion)):
    suma=0
    conteo=0
    for j in range(len(infeccion[i])):
        suma+=infeccion[i][j]
        conteo+=1
    promedio=suma/conteo
    if promedio>=70:
        mensaje="Zona roja ☠️ Evacuar"
    elif promedio>=40:
        mensaje="Zona naranja ⚠️ Precaución"
    else:
        mensaje="Zona verde ✅ Segura"
    print(f"{promedio}->{mensaje}")