print('*** Sistema De Cálculo Factorial ***')

try:
    # Lectura, Entrada O Ingreso De Datos
    user_number = int(input('Ingrese Un Número, Para Hallar El Factorial: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Condicional Para Válidar Números No Negativos
    if (user_number >= 0):
        index = 1
        factorial_accumulator = 1
        
        # Cálculo Factorial Con El Ciclo While
        while (index <= user_number):
            factorial_accumulator *= index
            index += 1
        
        # Mostrar Información Por Consola
        print(f'\nEl Factorial De {user_number} Es: {factorial_accumulator}')
    else:
        print('\nNo Existe El Factorial De Números Negativos.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')