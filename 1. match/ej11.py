""" Desarrollar un programa en Python que clasifique el estado de salud 
de una persona según su Índice de Masa Corporal (IMC).
Rango de IMC            Clasificación
---------------------------------------
Menos de 18.5           Bajo peso
18.5 a 24.9             Peso normal
25.0 a 29.9             Sobrepeso
30.0 o más              Obesidad
Valor negativo          No válido
El programa debe:

Solicitar el valor del IMC de la persona (número decimal).
Clasificar el estado de salud usando match / case con guardas condicionales.
Mostrar la clasificación correspondiente según el rango del IMC.
Si el valor ingresado es negativo, mostrar un mensaje de valor no válido.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar. """
try:
    valor_IMC=float(input("Ingrese número decimal: "))
except Exception:
    print("Error...")
else:
    match valor_IMC:
        case valor_IMC if valor_IMC<18.5:
            print("Bajo peso")
        case valor_IMC if 18.5<=valor_IMC<=24.9:
            print("Peso normal")
        case valor_IMC if 25<=valor_IMC<=29.9:
            print("Sobrepeso")
        case valor_IMC if valor_IMC>=30:
            print("Obesidad")
        case _:
            print("No válido")