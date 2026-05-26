""" Desarrollar un programa en Python que indique la velocidad máxima 
permitida de conducción según el estado del clima y el tipo de vía.
Clima           Vía             Velocidad Máxima
-------------------------------------------------
Lluvioso        Autopista       80 km/h
Lluvioso        Ciudad          40 km/h
Soleado         Autopista       120 km/h
Soleado         Ciudad          60 km/h
El programa debe:

Solicitar el estado del clima (Lluvioso / Soleado).
Solicitar el tipo de vía (Autopista / Ciudad).
Determinar la velocidad máxima permitida según la combinación de clima y vía.
Si los datos ingresados no corresponden a ninguna combinación válida, mostrar 
un mensaje de datos no válidos.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
Solo son válidas las combinaciones exactas de clima y vía descritas en la tabla.
Cualquier otro valor ingresado debe considerarse no válido. """
while True:
    try:
        estado_clima=int(input("Ingrese el estado del clima ((1) Lluvioso / (2) Soleado): "))
        if estado_clima<1 or estado_clima>2:
            print("Tiene que ser 1 o 2")
            continue
        tipo_via=int(input("Ingrese el tipo de vía ((1) Autopista  / (2) Ciudad): "))
        if tipo_via<1 or tipo_via>2:
            print("Tiene que ser 1 o 2")
            continue
    except ValueError:
        print("Las opciones tienen que ser números, no cadena de texto.")
    else:
        if (estado_clima==1 and tipo_via==1):
            print("80 Km/h")
        elif (estado_clima==1 and tipo_via==2):
            print("40 Km/h")
        elif (estado_clima==2 and tipo_via==1):
            print("120 Km/h")
        elif (estado_clima==2 and tipo_via==2):
            print("60 Km/h")
        while True:
            try:
                opciones=int(input("¿Desea Continuar? (1) Si / (2) No: "))
                if opciones<1 or opciones>2:
                    raise ValueError
                break
            except ValueError:
                print("Las opciones tiene que ser 1 o 2")
        if opciones!=1:
            break    
    finally:
        print("Ejecución terminada")