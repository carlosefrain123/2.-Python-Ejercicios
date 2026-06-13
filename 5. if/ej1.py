""" Desarrollar un programa en Python que determine si un número entero es par o impar,
usando el operador ternario.
El programa debe:

Solicitar al usuario un número entero.
Determinar si el número es par o impar usando el operador ternario.
Mostrar el número ingresado junto con su clasificación.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar el operador ternario para determinar si el número es par o impar.
Usar la estructura try / except / else / finally.
Un número es par si el residuo de dividirlo entre 2 es igual a 0. """
try:
    numero=int(input("Ingrese un número: "))
except Exception:
    print("Error...")
else:
    mensaje="par" if numero%2==0 else "numero impar"
    print(mensaje)
finally:
    print("Ejecución Terminada")
    