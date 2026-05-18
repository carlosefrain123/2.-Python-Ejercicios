""" Ejercicio: Calculadora de Tarifa de Estacionamiento
Desarrollar un programa en Python que calcule el costo total de un estacionamiento según el tipo de vehículo y las horas estacionado. Las tarifas son las siguientes:
Vehículo        Tarifa por Hora       Cargo Extra (más de 12h)
--------------------------------------------------------------
Moto            $1.50 por hora        $5.00 adicionales
Auto            $2.50 por hora        $5.00 adicionales
Autobús         $4.00 por hora        $5.00 adicionales
El programa debe:

Solicitar las horas estacionado (número decimal).
Solicitar el tipo de vehículo (Moto / Auto / Autobús).
Calcular la tarifa base multiplicando el precio por hora según el vehículo.
Si las horas superan las 12 horas, agregar un cargo extra de $5.00.
Calcular el total a pagar sumando la tarifa base más el cargo extra.
Mostrar un resumen con las horas, tipo de vehículo, tarifa base, cargo extra y total a pagar.
Si el vehículo no es reconocido o las horas son negativas, mostrar un mensaje de datos no válidos.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar, sin importar si hubo error o no.

Consideraciones:

Usar la estructura try / except / else / finally.
La tarifa base se calcula multiplicando las horas por el precio según el tipo de vehículo.
El cargo extra de $5.00 aplica únicamente si las horas superan las 12.
Las horas negativas y los vehículos no reconocidos no son válidos. """
while True:
    try:
        vehiculo=int(input("Ingrese el tipo de vehículo (1. Moto / 2. Auto / 3. Autobús): "))
        if vehiculo<1 or vehiculo>3:
            print("====Las opciones son del 1 al 3.====")
            continue
        hora=float(input("Ingrese las horas estacionadas: "))
        if hora<0 or hora>24:
            print("====Las horas no tiene que ser mayor a o menor a 24 horas.====")
            continue
    except ValueError:
        print("Tienen que ser número, no cadenas de textos.")
    except Exception as e:
        print(f"Detalle: {e}")
    else:
        cargo_extra=0
        if vehiculo==1:
            tarifa=1.50*hora
        if vehiculo==2:
            tarifa=2.50*hora
        if vehiculo==3:
            tarifa=4*hora
        if hora>12:
            cargo_extra=5
        total=tarifa+cargo_extra
        print(f"Horas estacionada: {hora} horas")
        print(f"cargo Extra: {cargo_extra}")
        print(f"Total: S/ {total}")
        while True:
            try:
                opciones=int(input("¿Desea continuar? (1) Sí / (2) No: "))
                if opciones<1 or opciones>2:
                    raise ValueError
                break
            except ValueError:
                print("Las opciones deben ser 1 o 2.")
        if opciones!=1:
            break                
                