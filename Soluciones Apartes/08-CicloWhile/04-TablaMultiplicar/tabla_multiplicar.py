print('*** Tabla De Multiplicar De Un Número ***')

try:
    # Lectura De Datos Y Validación Inicial
    user_number = float(input('Ingrese Un Valor Numérico: '))
except Exception as error:
    print('\nError: Los Valores Ingresados No Son Válidos.')
    print(f'Detalle Del Error: {error}')
else:
    # Inicialización De Variables
    multiplier = 0
    
    # Estructura Cíclica While Para Generar La Tabla De Multiplicar
    while (multiplier <= 20):
        operation_result = user_number * multiplier
        print(f'{user_number} x {multiplier} = {operation_result}')
        multiplier += 1
finally:
    print('El Bloque De Código Termino Su Ejecución.')