""" Ejercicio 3: Identificador de Número Mayor y Menor
Desarrollar un programa en Python que determine cuál es el número mayor 
y cuál es el número menor entre tres valores ingresados por el usuario.
El programa debe:

Solicitar tres valores numéricos al usuario.
Determinar cuál de los tres es el número mayor.
Determinar cuál de los tres es el número menor.
Si todos los números son iguales, indicarlo tanto para el mayor como para el menor.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
El mayor y el menor se determinan de forma independiente.
Si los tres valores son iguales, se muestra un mensaje indicándolo en ambos casos. """
while True:
    try:
        valorA=int(input("Ingrese el valor A: "))
        if valorA<0:
            print("El valor A, no tiene que ser negativo")
        valorB=int(input("Ingrese el valor B: "))
        if valorB<0:
            print("El valor B, no tiene que ser negativo")
        valorC=int(input("Ingrese el valor C: "))
        if valorC<0:
            print("El valor C, no tiene que ser negativo")
    except ValueError:
        print("***Valor incorrecto***")
    else:
        maximo_valor=max(valorA,valorB,valorC)
        minimo_valor=min(valorA,valorB,valorC)
        print(f"El máximo valor es: {maximo_valor}")
        print(f"El minimo valor es: {minimo_valor}\n")
        while True:
            try:
                opciones=int(input("¿Desea Continuar? (1) Sí / (2) No: "))
                if opciones<1 or opciones>2:
                    raise ValueError
                break
            except ValueError:
                print("Tiene que ser 1 o 2")
        if opciones!=1:
            break
    finally:
        print("Ejecución Terminada\n")