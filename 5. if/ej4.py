""" Desarrollar un programa en Python que determine si un año es bisiesto o no, 
usando el operador ternario.
Un año es bisiesto si cumple una de estas condiciones:
Condición                                   Resultado
------------------------------------------------------
Divisible entre 4 y NO entre 100            Bisiesto
Divisible entre 400                         Bisiesto
Cualquier otro caso                         No bisiesto
El programa debe:

Solicitar al usuario un año (número entero positivo).
Determinar si el año es bisiesto o no usando el operador ternario.
Mostrar el resultado indicando Sí o No.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar el operador ternario para determinar si el año es bisiesto.
Usar la estructura try / except / else / finally.
Solo se aceptan años mayores a 0. """
try:
    year=int(input("Ingrese año: "))
except Exception:
    print("Error...")
else:
    mensaje="Bisiesto" if (year%4==0 and year%100!=0) or (year%400==0) else "No bisiesto"
    print(mensaje)
finally:
    print("Ejecución Terminada.")