try:
    # Lectura, Entrada O Ingreso De Datos (Inicialización)
    license_plate = input('Ingrese La Placa Del Autobus: ')
    number_passengers = int(input('Ingrese La Cantidad De Pasajeros Transportados: '))
    route = input('Ingrese La Ruta Prestada (A o B): ')
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Condicional Compuesto Valores Negativos
    if (number_passengers >= 0):
        # Estructura Condicional Anidado
        if ((route == 'A') or (route == 'a')):
            # Operaciones Aritméticas
            ticket_value = 10
            service_value = number_passengers * ticket_value
        elif ((route == 'B') or (route == 'b')):
            # Operaciones Aritméticas
            ticket_value = 12
            service_value = number_passengers * ticket_value
        else:
            route = 'No Aplica'
            ticket_value = 0
            service_value = 0
            print('\nLa Ruta Ingresada No Es Válida.')

        # Mostrar Información Por Consola
        print(f'\nPlaca Del Autobus: {license_plate}')
        print(f'Número De Pasajeros: {number_passengers}')
        print(f'Ruta Prestada (A o B): {route}')
        print(f'Valor Del Pasaje: {ticket_value} Dólares.')
        print(f'Dinero Recolectado En El Trayecto: {service_value} Dólares.')
    else:
        print('\nEl Valor Ingresado No Es Válido.')
finally:
    print('El Bloque De Código Termino Su Ejecución.\n')