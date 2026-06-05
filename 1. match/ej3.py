""" Desarrollar un programa en Python que calcule el área o perímetro de una figura geométrica
según la figura seleccionada por el usuario.
Figura          Dato requerido          Cálculo
------------------------------------------------------
Círculo         Radio                   Área = π × radio²
Cuadrado        Lado                    Perímetro = 4 × lado
Triángulo       Base y altura           Área = (base × altura) / 2
El programa debe:

Solicitar el nombre de la figura (Círculo / Cuadrado / Triángulo).
Solicitar los datos necesarios según la figura seleccionada.
Calcular y mostrar el resultado correspondiente según la figura.
Si la figura ingresada no es soportada, mostrar un mensaje de figura no válida.
Manejar excepciones en caso de que los valores numéricos no sean válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura match / case combinada con try / except / else / finally.
El valor de π utilizado es 3.1416.
Para el círculo se calcula el área, para el cuadrado el perímetro y para el triángulo el área. """
from math import pi
figura=input("Ingrese el nombre de la figura (Círculo / Cuadrado / Triángulo): ").lower()
resultado=0
match(figura):
    case "circulo":
        print("****Selecciono la figura circulo****")
        radio=float(input("Ingrese el radio: "))
        resultado=pi*(radio)**2
    case "cuadrado":
        print("****Selecciono la figura cuadrado****")
        lado=int(input("Ingrese el lado del cuadrado: "))
        resultado=4*lado
    case "triangulo":
        print("****Selecciono la figura de un triángulo****")
        base=int(input("Ingrese la base de un triángulo: "))
        altura=int(input("Ingrese la altura de un triangulo: "))
        resultado=(base*altura)/2
print(f"El resultado es: {round(resultado,2)}")