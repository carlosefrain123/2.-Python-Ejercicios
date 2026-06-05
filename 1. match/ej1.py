""" Desarrollar un programa en Python que indique la acción que debe realizar un conductor según el color del semáforo.
Color           Acción
--------------------------------
Rojo            Detener el vehículo
Amarillo        Reducir la velocidad
Verde           Avanzar con precaución
Otro valor      Color no reconocido
El programa debe:

Solicitar el color del semáforo al usuario.
Mostrar la acción correspondiente según el color ingresado.
Si el color no es reconocido, mostrar un mensaje de color no válido.

Consideraciones:

Usar la estructura match / case.
Este ejercicio no requiere manejo de excepciones con try / except. """
color = input('Color Del Semáforo: ').lower()
match(color):
    case "rojo":
        print("Detener el vehículo")
    case "amarillo":
        print("Reducir la velocidad")
    case "verde":
        print("Avanzar con precaución")
    case _:
        print("Color no reconocido")