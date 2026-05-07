print('****** Sistema De Rango Numérico Ascendente (De Menos A Más) ******')

try:
    # Lectura De Datos Y Validación Inicial
    initial_number = int(input('Ingrese El Número Inicial Del Rango: '))
    final_number = int(input('Ingrese El Número Final Del Rango: '))
except Exception as error:
    print('\nError: Los Valores Ingresados No Son Válidos.')
    print(f'Detalle Del Error: {error}')
else:
    # Validación De Rango Numérico
    if (initial_number <= final_number):
        # Estructura Cíclica while Para El Rango Numérico
        while (initial_number <= final_number):
            print(initial_number, end = ' ')
            initial_number += 1
    else:
        print('\nNo Es Posible Desarrollar El Ejercicio Algorítmico.')
finally:
    print('\nEl Bloque De Código Termino Su Ejecución.')