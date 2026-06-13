""" Desarrollar un programa en Python que aplique un descuento del 10% sobre 
una compra si el valor supera los $200.00, usando el operador ternario.
Valor de Compra         Descuento
-----------------------------------
Mayor a $200.00         10% de descuento
$200.00 o menos         Sin descuento
El programa debe:

Solicitar el valor de la compra en dólares.
Aplicar un descuento del 10% si la compra supera los $200.00, usando el operador ternario.
Mostrar el total a pagar tras aplicar o no el descuento.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar el operador ternario para aplicar o no el descuento.
Usar la estructura try / except / else / finally.
El descuento se calcula siempre sobre el valor original de la compra. """
try:
    vc=int(input("Ingrese el valor de la compra: "))
except Exception:
    print("Error...")
else:
    mensaje=vc-(vc*0.1) if vc>200 else vc
    print(mensaje)
finally:
    print("Ejecución Terminada.")