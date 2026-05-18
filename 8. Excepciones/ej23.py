""" Verificador de Múltiplos
Desarrollar un programa en Python que determine si un número ingresado es múltiplo de
3, de 5, o de ambos.
El programa debe:

Solicitar al usuario un valor numérico.
Verificar si el número es múltiplo de 3 y/o múltiplo de 5.
Mostrar un mensaje indicando cuál de las condiciones se cumple.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
Un número puede ser múltiplo de 3, de 5, o de ambos al mismo tiempo.
Si no es múltiplo de ninguno, no se muestra ningún mensaje adicional. """
while True:
    try:
        valor=int(input("Ingrese el valor numérico: "))
        if valor<0:
            print("El valor no tiene que ser negativo.")
            continue
    except ValueError:
        print("El valor tiene que ser un número, no una cadena de texto")
    except Exception as e:
        print("Error...")
        print(f"Detalle: {e}")
    else:
        multiplo_3=valor%3==0
        multiplo_5=valor%5==0
        if multiplo_3 and multiplo_5:
            print("Es multiplo de 3 y 5")
        elif multiplo_5:
            print("Es multiplo de 5")
        elif multiplo_3:
            print("Es multiplo de 3")
        while True:
            try:
                opcion=int(input("¿Desea continuar? (1)Sí / (2)No: "))
                if opcion not in(1,2):
                    raise ValueError
                break
            except ValueError:
                print("Tienen que ser 1 o 2. No una cadena de texto")
            except Exception as e:
                print(f"Detalle: {e}")
        if opcion!=1:
            break
    