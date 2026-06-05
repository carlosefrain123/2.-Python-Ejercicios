""" Desarrollar un programa en Python que muestre un menú de opciones y registre el color favorito del usuario según la opción elegida.
Opción          Color
----------------------
1               Rojo
2               Amarillo
3               Azul
4               Verde
5               Otro
Otro valor      No válido
El programa debe:

Mostrar un menú de opciones con los colores disponibles.
Solicitar al usuario que elija una opción del menú.
Mostrar el color favorito correspondiente a la opción seleccionada.
Si la opción no es válida, mostrar un mensaje de opción no válida.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura match / case combinada con try / except / else / finally. """
print("------Menú------")
print("(1) Rojo (2) Amarillo (3) Azul (4) Verde (5) Otro ")
try:
    opcion_color=int(input("Ingrese la opción del menú: "))
except Exception:
    print("Error...")
else:
    match opcion_color:
        case 1:
            print("Rojo")
        case 2:
            print("Amarillo")
        case 3:
            print("Azul")
        case 4:
            print("Verde")
        case 4:
            print("Otro")
        case _:
            print("No existe valor")
finally:
    print("Ejecución Terminada.")