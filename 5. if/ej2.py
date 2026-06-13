""" Desarrollar un programa en Python que determine si una persona está habilitada 
para votar según su edad, usando el operador ternario.
Edad                Resultado
------------------------------
16 años o más       Puede votar
Menos de 16 años    No puede votar
Fuera de rango      No válido
El programa debe:

Solicitar la edad de la persona.
Determinar si la persona puede o no votar usando el operador ternario.
Si la edad está fuera del rango de 0 a 120, mostrar un mensaje de edad no válida.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar el operador ternario para determinar si puede votar.
Usar la estructura try / except / else / finally.
La edad mínima para votar es de 16 años. """
try:
    edad=int(input("Ingrese su edad: "))
except Exception:
    print("Error...")
else:
    if(edad>0 and edad<120):
        mensaje="Puede Votar" if edad>=16 else "No puede votar"
        print(mensaje)
    else:
        print("Fuera de rango, no válido.")
finally:
    print("Ejecución Terminada.")