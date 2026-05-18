""" Ejercicio: Calculadora de Peaje
Desarrollar un programa en Python que calcule el costo del peaje según el tipo de vehículo. En una autopista, 
la tarifa varía de la siguiente manera:

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
        num_ejes=int(input("Ingrese el número de ejes: "))
        if num_ejes<0:
            print("No tiene que ser negativo")
            continue
        tip_vehi=int(input("Ingrese el tipo de vehículo ((1) Motocicleta / (2) Automóvil / (3) Camión)."))
        if tip_vehi<0 or tip_vehi>3:
            print("Tiene que se de 1 a 3 las opciones.")
            continue
    except ValueError:
        print("Tienen que ser números, no cadenas de textos.")
    except Exception as e:
        print(f"Detalle: {e}")
    else:
        tarifa=0
        if tip_vehi==1:
            tarifa=1.50
        elif tarifa==2:
            tarifa=3.00
        else:
            tarifa=5.00*num_ejes
        print(f"La tarifa es: {tarifa}")
        
        while True:
            try:
                opciones=int(input("¿Desea continuar? (1) Sí / (2) No: "))
                if opciones<1 or opciones>2:
                    raise ValueError
                break
            except ValueError:
                print("Las opciones tienen que ser 1 o 2")
        if opciones!=1:
            break
    finally:
        print("Ejecución Terminada.")
    