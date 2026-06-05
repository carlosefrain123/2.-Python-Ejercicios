""" Ejercicio 5: Clasificador de Mayor o Menor de Edad
Desarrollar un programa en Python que determine si una persona es mayor o menor de edad según la edad ingresada.
Rango de Edad       Clasificación
-----------------------------------
0 a 17 años         Menor de edad
18 a 120 años       Mayor de edad
Fuera de rango      No válido
El programa debe:

Solicitar la edad de la persona.
Determinar si la persona es mayor o menor de edad según el rango.
Si la edad está fuera del rango de 0 a 120, mostrar un mensaje de valores no válidos.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar. """
try:
    edad=int(input("Ingrese su edad: "))
except Exception as e:
    print("Error...")
else:
    match edad:
        case edad if edad<=17:
            print("Menor de edad.")
        case edad if edad<=120:
            print("Mayor de edad")
        case _:
            print("No valido")
finally:
    print("Ejecución Terminada")