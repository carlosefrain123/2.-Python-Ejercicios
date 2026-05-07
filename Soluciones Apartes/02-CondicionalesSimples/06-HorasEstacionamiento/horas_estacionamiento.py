try:
    # Lectura, Entrada O Ingreso De Datos
    hours = float(input('Horas Estacionado: '))
    vehicle = input('Tipo De Vehículo (Moto / Auto / Autobus): ').lower()
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Definir E Inicializar Variables Y/O Constantes
    fee = 0
    valid = True
    additional = 0
    
    # Verificamos La Tarifa Base Dependiendo Del Vehículo
    if (vehicle == 'moto'):
        fee = 1.50 * hours

    if (vehicle == 'auto'):
        fee = 2.50 * hours

    if (vehicle == 'autobus'):
        fee = 4.00 * hours
    
    # Verificamos Si Existe El Tiempo Extra
    if (hours > 12):
        additional = 5.00
    
    # Operatividad Y Procesos (SUMA)
    total = fee + additional
    
    # Si El Usuario Ingresa Valores No Funcionales Se Activa Este Condicional
    if (fee == 0 or hours < 0):
        valid = False
        print('\nEl Vehículo Ingresado No Es Válido O Las Horas No Son Válidas.')
    
    # Si El Desarrollo De Los Datos Y La Operatividad Se Hace Exitosamente Se Muestra Información
    if (valid):
        print(f'\nHoras Estacionamiento: {hours}.')
        print(f'Tipo De Vehículo (Moto / Auto / Autobus): {vehicle}.')
        print(f'Tarifa Base: {fee} Dólares.')
        print(f'Cargo Extra: {additional} Dólares.')
        print(f'Total A Pagar: {total} Dólares.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')