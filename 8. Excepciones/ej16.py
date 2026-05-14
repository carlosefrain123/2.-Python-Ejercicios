""" Ejercicio: Calculadora de Peaje
Desarrollar un programa en Python que calcule el costo del peaje según el tipo de vehículo. En una autopista, la tarifa varía de la siguiente manera:

Motocicletas: $1.50
Automóviles: $3.00
Camiones/Buses: $5.00 por eje

El programa debe:

Solicitar al usuario el número de ejes del vehículo.
Solicitar el tipo de vehículo (Motocicleta / Automóvil / Camión).
Calcular el total a pagar según la categoría.
Manejar excepciones en caso de que el usuario ingrese valores no válidos.
Mostrar siempre un mensaje de finalización al terminar el programa, sin importar si ocurrió un error o no.

Consideraciones:

Usar la estructura try / except / else / finally.
Si el tipo de vehículo ingresado no corresponde a ninguna categoría, mostrar un mensaje de categoría no válida.
El costo de los camiones/buses se multiplica por el número de ejes. """
while True:
    try:
        num_ejes=int(input("***Ingrese el número de ejes de su vehículo: "))
        if num_ejes<0: 
            print("====El número de ejes no tiene que ser negativo====") 
            continue
        tip_vehiculo=int(input("\n**Ingrese el tipo de vehículo: (1. Motocicleta / 2. Automóvil / 3. Camión)"))
        if tip_vehiculo<1 or tip_vehiculo>3: 
            print("====Las opciones tienen que ser 1, 2 u 3====")
            continue
    except ValueError:
        print("Error... Deben ser número, no cadenas de textos")
    except Exception as e:
        print("Error...")
        print(f"Detalle: {e}")
    else:
        if tip_vehiculo==1:
            tarifa=1.50
        if tip_vehiculo==2:
            tarifa=3.00
        if tip_vehiculo==3:
            tarifa=5.00*num_ejes
        print(f"Número de ejes: {num_ejes}")
        print(f"Tipo de vehículo: {tip_vehiculo}")
        print(f"La tarifa es: {tarifa}")
    finally:
        print("Ejecución Terminada,")