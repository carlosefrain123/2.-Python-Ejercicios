""" Ejercicio 2: Recaudación de Ingresos de Autobús por Ruta
Desarrollar un programa en Python que calcule el dinero recaudado por un 
autobús en un trayecto, según la ruta prestada y la cantidad de pasajeros transportados.
Ruta        Valor del Pasaje
-----------------------------
Ruta A      $10.00 por pasajero
Ruta B      $12.00 por pasajero
El programa debe:

Solicitar la placa del autobús.
Solicitar la cantidad de pasajeros transportados.
Solicitar la ruta prestada (A o B).
Calcular el dinero recaudado multiplicando los pasajeros por el valor del pasaje según la ruta.
Mostrar un resumen con la placa, número de pasajeros, ruta, valor del pasaje y dinero recaudado.
Si la ruta ingresada no es válida, mostrar un mensaje de ruta no válida.
Si la cantidad de pasajeros es negativa, mostrar un mensaje de valor no válido.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
Solo son válidas las rutas A y B.
La cantidad de pasajeros no puede ser negativa. """
while True:
    try:
        placa=input("Ingrese la placa del autobus: ")
        cant_pasajeros=int(input("Ingrese la cantidad de pasajeros transportados: "))
        if cant_pasajeros<0:
            print("El valor no tiene que ser negativo")
            continue
        rutas=int(input("Ingrese la ruta a escoger (1) Ruta A / (2) Ruta B: "))
        if rutas<1 or rutas>2:
            print("El valor no tiene ")
            continue
    except ValueError:
        print("Los datos son incorrectos")
    else:
        pasaje=0
        if rutas==1:
            pasaje=10
        else:
            pasaje=12
        total=pasaje*cant_pasajeros
        print(f"Placa del autobus: {placa}")
        print(f"Número de Pasajeros: {cant_pasajeros}")
        print(f"Valor de pasaje: {pasaje}")
        print(f"Dinero recaudado: {total}")
        while True:
            try:
                opciones=int(input("¿Desea Continuar? (1) Sí / (2) No: "))
                if opciones<1 or opciones>2:
                    raise ValueError
                break
            except ValueError:
                print("Tiene que ser 1 o 2")
        if opciones!=1:
            break
    finally:
        print("Ejecución Terminada")