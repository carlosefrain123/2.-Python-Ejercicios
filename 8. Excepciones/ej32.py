""" Ejercicio 2: Clasificador de Números Pares e Impares
Desarrollar un programa en Python que determine si un número ingresado por el usuario es par o impar.
El programa debe:

Solicitar al usuario un valor numérico.
Determinar si el número es par o impar usando el operador módulo.
Mostrar el valor ingresado junto con su clasificación.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
Un número es par si el residuo de dividirlo entre 2 es igual a 0, de lo contrario es impar. """
while True:
    try: 
        valor=int(input("Ingrese un número: "))
        if valor<0:
            print("Los valores no tienen que ser negativos.")
            continue
    except ValueError:
        print("El valor no tiene que ser negativo")
    else:
        if valor%2==0:
            print("Número par")
        else:
            print("Número Impar")
        while True:
            try:
                opcion=int(input("¿Desea Continuar? (1) Sí / (2) No"))
                if opcion<1 or opcion>2:
                    raise ValueError
                break
            except ValueError:
                print("El valor tiene que ser de 1 o 2")
        if opcion!=1:
            break