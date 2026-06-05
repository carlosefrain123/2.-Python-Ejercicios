""" Desarrollar un programa en Python que muestre el nombre del día de la semana según el número ingresado por el usuario.
Número          Día
--------------------
1               Lunes
2               Martes
3               Miércoles
4               Jueves
5               Viernes
6               Sábado
7               Domingo
Otro valor      No válido
El programa debe:

Solicitar al usuario un número del 1 al 7.
Mostrar el día de la semana correspondiente al número ingresado.
Si el número está fuera del rango, mostrar un mensaje de valor no válido.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura match / case combinada con try / except / else / finally. """
try:
    num_dia=int(input("Ingrese el número de día de la semana: "))
except:
    print("Error..")
else:
    match(num_dia):
        case 1:
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miercoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6:
            print("Sábado")
        case 7:
            print("Domingo")
        case _:
            print("Debe ser del 1 al 7")
finally:
    print("Ejecución Terminada.")