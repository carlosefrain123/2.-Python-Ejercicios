""" Desarrollar un programa en Python que determine el precio de entrada
a un evento según la edad del asistente, usando el operador ternario.
Edad                    Precio
--------------------------------
Menor de 12 años        $5.00
12 años o más           $15.00
Fuera de rango          No válido
El programa debe:

Solicitar la edad del asistente.
Determinar el precio de entrada usando el operador ternario.
Mostrar la edad ingresada y el precio final a pagar.
Si la edad está fuera del rango de 0 a 120, mostrar un mensaje de edad no válida.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar el operador ternario para asignar el precio según la edad.
Usar la estructura try / except / else / finally. """
try:
    edad=int(input("Ingrese su edad: "))
except Exception:
    print("Error")
else:
    if 0<=edad<=120: 
        mensaje=5 if edad<12 else 15
    else:
        print("No válido")
    print(f"Edad: {edad}")
    print(f"Costo: ${mensaje}")
finally:
    print("Ejecución Terminada.")
    
    