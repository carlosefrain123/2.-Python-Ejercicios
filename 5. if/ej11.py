""" Desarrollar un programa en Python que clasifique el rendimiento 
de un vehículo según los kilómetros recorridos por litro de combustible, 
usando el operador ternario encadenado.
Rendimiento (km/l)      Clasificación
---------------------------------------
Menos de 8              Consumo Excesivo
8 a 12                  Consumo Regular
13 a 18                 Consumo Eficiente
Más de 18               Consumo Óptimo
Valor negativo          No válido
El programa debe:

Solicitar el rendimiento del vehículo en km/l (número decimal).
Clasificar el rendimiento usando el operador ternario encadenado.
Mostrar la clasificación correspondiente según el rendimiento ingresado.
Si el valor ingresado es negativo, mostrar un mensaje de valor no válido.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar el operador ternario encadenado para clasificar el rendimiento.
Usar la estructura try / except / else / finally.
El rendimiento no puede ser un valor negativo. """
try:
    rendimiento=int(input("Ingrese el rendimiento: "))
except Exception:
    print("Error...")
else:
    mensaje="Consumo Excesivo" if rendimiento<8 else "Consumo Regular" if 8<=rendimiento<=12 else "Consumo Eficiente" if 13<=rendimiento<=18 else "Consumo Óptimo" if rendimiento>18 else "No válido"
    print(mensaje)
