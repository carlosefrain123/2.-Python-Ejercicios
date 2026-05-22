""" Tienes el registro de temperatura de 3 ciudades
durante 4 días.
Tu tarea es:
1. Calcular el promedio de temperatura de cada ciudad
2. Encontrar la temperatura más alta y más baja de cada ciudad
3. Clasificar cada ciudad:
   promedio >= 25 → "Calurosa 🥵"
   promedio >= 15 → "Templada 😊"
   promedio <  15 → "Fría 🥶" """
temperaturas = [
    [28, 30, 27, 29],   # Lima
    [10, 12, 11, 13],   # Cusco
    [22, 24, 23, 21],   # Arequipa
]
ciudades = ["Lima", "Cusco", "Arequipa"]

print("1. Calcular el promedio de temperatura de cada ciudad")
for i in range(len(temperaturas)):
    suma_temp=0
    conteo=0
    for j in range(len(temperaturas[i])):
        suma_temp=temperaturas[i][j]
        conteo+=1
    promedio=suma_temp/conteo
    print(ciudades[i],"->",promedio,"C°")
    
print("2. Encontrar la temperatura más alta y más baja de cada ciudad")
for i in range(len(temperaturas)):
    temp_alta=0
    temp_baja=temperaturas[0][0]
    for j in range(len(temperaturas[i])):
        if temperaturas[i][j]>temp_alta:
            temp_alta=temperaturas[i][j]
        if temperaturas[i][j]<temp_baja:
            temp_baja=temperaturas[i][j]
    print("Temp. Alta",ciudades[i],"->",temp_alta,"C°")
    print("Temp. Baja",ciudades[i],"->",temp_baja,"C°")
print("3")
for i in range(len(temperaturas)):
    suma_temp=0
    conteo=0
    for j in range(len(temperaturas[i])):
        suma_temp=temperaturas[i][j]
        conteo+=1
    promedio=suma_temp/conteo
    if promedio>=25:
        respuesta="Caluroso"
    elif promedio>=15:
        respuesta="Templada"
    elif promedio<15:
        respuesta="Fría"
    print(ciudades[i],"->",promedio,"C°","->",respuesta)