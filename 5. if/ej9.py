""" Ejercicio 4: Conversión de Nota Numérica a Literal con Operador Ternario
Desarrollar un programa en Python que convierta una calificación 
numérica a su equivalente en letra, usando el operador ternario encadenado.
Nota Numérica       Calificación Literal
------------------------------------------
5                   A
4                   B
3                   C
2                   D
1 o menos           F
Fuera de rango      No válido
El programa debe:

Solicitar una nota entera del 1 al 5.
Convertir la nota numérica a su calificación literal usando el operador ternario encadenado.
Mostrar la nota numérica y la calificación literal correspondiente.
Si la nota está fuera del rango de 0 a 5, mostrar un mensaje de rango no válido.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar el operador ternario encadenado para asignar la calificación literal.
Usar la estructura try / except / else / finally.
El rango válido de notas es de 0 a 5. """
try:
    nota=int(input("Ingrese la nota: "))
except Exception:
    print("Error...")
else:
    if 0<=nota<=5:
        mensaje="F" if 0<=nota<=1 else "D" if nota==2 else "C" if nota==3 else "B" if nota==4 else "A"
        print(mensaje)
    else:
        print("Nota inválida")
finally:
    print("Ejecución Terminada")