""" Ejercicio 1: Registro de ciudades y temperaturas
Un programa que:

Pide nombres de ciudades y sus temperaturas
Guarda todo en un diccionario
Al final muestra los ciudades ordenadas y el promedio de sus temperaturas"""
diccionario={}
while True:
    try:
        ciudad=input("Ingrese la ciudad: ")
        if ciudad=="":
            break
        temperatura=float(input("Ingrese la temperatura: "))
        if temperatura not in range(0,101):
            break
    except Exception as e:
        print("Error..")
        print(f'Detalle del error e: {e}')
    else:
        if ciudad in diccionario:
            print("Ciudad ya registrada")
            diccionario[ciudad]+=(temperatura,)
        else:
            print("Registrando...")
            diccionario[ciudad]=(temperatura,)
    finally:
        print("Terminó ejecución")
""" print(diccionario) """
for ciudad in sorted(diccionario.keys()):
    total=0
    conteo=0
    """ print(ciudad) """
    for temperatura in diccionario[ciudad]:
        total+=temperatura
        conteo+=1
    promedio=total/conteo
    print(f'La ciudad {ciudad} su promedio es: {promedio}')
        