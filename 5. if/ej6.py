""" Desarrollar un programa en Python que clasifique el
estado del clima según la temperatura ingresada, usando el operador ternario encadenado.
Temperatura             Estado
--------------------------------
0°C o menos             Congelado
Entre 1°C y 14°C        Frío
Entre 15°C y 24°C       Templado
25°C o más              Caliente
El programa debe:

Solicitar la temperatura actual en grados Celsius.
Clasificar el estado del clima usando el operador ternario encadenado.
Mostrar el estado del clima correspondiente.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar el operador ternario encadenado para clasificar la temperatura.
Usar la estructura try / except / else / finally. """
try:
    temp=int(input("Ingrese la temperatura: "))
except Exception:
    print("Error...")
else:
    mensaje="Congelado" if temp<=0 else "Frio" if 1<=temp<=14 else "Templado" if 15<=temp<=24 else "Caliente"
    print(mensaje)
finally:
    print("Ejecución Terminada.")
    