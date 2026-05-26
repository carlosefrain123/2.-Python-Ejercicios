""" Ejercicio 4: Calculadora de Impuesto para Vehículos
Desarrollar un programa en Python que calcule el impuesto 
a pagar por un vehículo según su tipo y precio base.
Tipo            Precio Base         Impuesto
------------------------------------------------------
Eléctrico       Hasta $30,000       5%
Eléctrico       Más de $30,000      8%
Híbrido         Hasta $25,000       10%
Híbrido         Más de $25,000      15%
Combustión      Hasta $20,000       20%
Combustión      Más de $20,000      25%
El programa debe:

Solicitar el tipo de vehículo (Eléctrico / Híbrido / Combustión).
Solicitar el precio base del vehículo en dólares.
Calcular el impuesto según el tipo y el precio del vehículo.
Calcular el precio final sumando el precio base más el impuesto.
Mostrar el impuesto calculado y el precio final.
Si el tipo de vehículo no es válido o el precio es negativo, mostrar un mensaje de datos no válidos.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
El impuesto varía según el tipo de vehículo y su precio base.
El precio base debe ser mayor a cero. """
while True:
    try:
        tipo_vehiculo=int(input("Tipo de vehículo ((1) Eléctrico / (2) Híbrido / (3) Combustión): "))
        if tipo_vehiculo<1 or tipo_vehiculo>3:
            print("****Tiene que ser de 1 a 3****")
            continue
        precio_base=float(input("Ingrese el precio base del vehículo en dólares: "))
        if precio_base<0:
            print("****No tiene que ser negativo el valor****")
            continue
    except ValueError:
        print("***Los valores no tienen que ser cadena de texto***")
    else:
        impuesto=0
        if tipo_vehiculo==1 and precio_base<=30000:
            impuesto=5
        elif tipo_vehiculo==1 and precio_base>30000:
            impuesto=8
        elif tipo_vehiculo==2 and precio_base<=25000:
            impuesto=10
        elif tipo_vehiculo==2 and precio_base>25000:
            impuesto=15
        elif tipo_vehiculo==3 and precio_base<=20000:
            impuesto=20
        elif tipo_vehiculo==3 and precio_base>20000:
            impuesto=25
        impuesto/=100
        impuesto_generado=precio_base*impuesto
        total=precio_base+(impuesto_generado)
        print(f"Precio Base: {precio_base}")
        print(f"Impuesto: {impuesto*100}")
        print(f"Impuesto Generado: {impuesto_generado}")
        print(f"Precio Final: {total}")
        while True:
            try:
                opciones=int(input("¿Desea Continuar? (1) Si / (2) No: "))
                if opciones<1 or opciones>2:
                    print("Las opciones tiene que ser 1 o 2")
                break
            except ValueError:
                print("Las opciones tiene que ser 1 o 2")
        if opciones!=1:
            break
    finally:
        print("Ejecución Terminada")