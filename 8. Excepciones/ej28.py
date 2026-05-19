""" Monitor de Temperatura y Humedad
Desarrollar un programa en Python que evalúe las condiciones ambientales de temperatura y humedad, emitiendo alertas si los valores se encuentran fuera de los rangos seguros.
Variable        Rango Seguro       Alerta
------------------------------------------------------
Temperatura     5°C a 35°C         Fuera del rango
Humedad         80% o menos        Mayor al 80%
El programa debe:

Solicitar la temperatura actual en grados Celsius.
Solicitar la humedad relativa en porcentaje.
Si la temperatura supera los 35°C, mostrar alerta de temperatura extremadamente alta.
Si la temperatura es menor a 5°C, mostrar alerta de temperatura extremadamente baja.
Si la temperatura está entre 5°C y 35°C, indicar que está dentro del rango seguro.
Si la humedad supera el 80%, mostrar alerta de humedad muy elevada.
Si la humedad es 80% o menos, indicar que está dentro del rango aceptable.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
La temperatura y la humedad se evalúan de forma independiente.
Pueden activarse alertas de temperatura y humedad al mismo tiempo. """
while True:
    try:
        temperatura=int(input("Ingrese la temperatura actual en grados Celsius: "))
        porce_humedad=float(input("Ingrese la humedad relativa en porcentaje: "))
        if porce_humedad<0 or porce_humedad>100:
            print("El porcentaje no tiene que ser negativo o mayor a 100%.")
            continue
    except ValueError:
        print("Los valores debe ser números, no cadenas de texto.")
    else:
        if temperatura>35:
            print('\n¡Alerta! Temperatura Extremadamente Alta (>35°C).')
        else:
            if temperatura<5:
                print('\n¡Alerta! Temperatura Extremadamente Baja (<5°C).')
            else:
                print('\nTemperatura Dentro Del Rango Seguro (5°C - 35°C).')
        if porce_humedad>80:
            print("Alerta de humedad muy elevado")
        else:
            print("Humedad muy baja")
        while True:
            try:
                opciones=int(input("¿Desea continuar? (1) Sí / (2) No: "))
                if opciones<1 or opciones>2:
                    raise ValueError
                break
            except ValueError:
                print("Las ocpiones tienen que ser 1 o 2")
        if opciones!=1:
            break
            