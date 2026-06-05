""" Desarrollar un programa en Python que indique el día de restricción vehicular (pico y placa) según el último dígito de la placa del vehículo.
Último dígito       Día de restricción
---------------------------------------
0 o 1               Lunes
2 o 7               Martes
9 o 4               Miércoles
5 o 3               Jueves
6 o 8               Viernes
Otro valor          No válido
El programa debe:

Solicitar el último dígito de la placa del vehículo.
Mostrar el día de restricción correspondiente según el dígito ingresado.
Si el dígito ingresado no corresponde a ningún caso, mostrar un mensaje de valor no válido.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura match / case con guardas condicionales, combinada con try / except / else / finally.
El último dígito debe ser un número entero del 0 al 9. """
print("(0 o 1) Lunes (2 o 7) Martes (9 o 4) Miercoles (5 o 3) Jueves (6 o 8) Viernes")
try:
    digito=int(input("Ingrese el dígito: "))
except Exception:
    print("Error...")
else:
    match digito:
        case digito if(digito==0 or digito==1):
            print("Lunes")
        case digito if(digito==2 or digito==7):
            print("Martes")
        case digito if(digito==9 or digito==4):
            print("Miercoles")
        case digito if(digito==5 or digito==3):
            print("Jueves")
        case digito if(digito==6 or digito==8):
            print("Viernes")
        case _:
            print("No válido")
finally:
    print("Ejecució Terminada.")