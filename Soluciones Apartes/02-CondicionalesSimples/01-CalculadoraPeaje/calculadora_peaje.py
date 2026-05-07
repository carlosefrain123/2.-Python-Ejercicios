try:
    number_of_axles = int(input('Número De Ejes: '))
    vehicle_type = input('Tipo De Vehículo (Motocicleta / Automovil / Autobus): ').lower()
except Exception as e:
    print('Los Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    fee = 0
    valid = True
    
    # Estructura Algorítmica De Condicionales Simples
    if (vehicle_type == 'motocicleta' or vehicle_type == 'moto'):
        fee = 1.50

    if (vehicle_type == 'automovil' or vehicle_type == 'auto'):
        fee = 3.00
    
    if (vehicle_type == 'autobus' or vehicle_type == 'bus'):
        fee = 5.00 * number_of_axles
    
    # Validar Si Tenemos Una Categoria Diferente De 0
    if (fee <= 0):
        print('\nLa Categoría Ingresada No Es Válida.')
        valid = False
    
    if (valid):
        print(f'\nCategoria Del Vehículo: {vehicle_type}')
        print(f'Total A Pagar: {fee} Dólares')
finally:
    print('El Bloque De Código Termino Su Ejecución.')