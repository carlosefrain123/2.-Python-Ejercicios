print('***** Mostrar Distribución De Asientos Con Letras y Números *****')

try:
    # Lectura, Entrada O Ingreso De Datos
    sections = int(input('Ingrese El Número De Secciones: '))  
    
    # Condicional Para Válidar Los Datos Ingresados
    if (sections < 1):
        raise Exception('Las Cantidad De Secciones No Es Válida.')  

    # Estructura Algorítmica Cíclica (for Anidado)
    for index in range(1, sections + 1):
        rows = int(input(f'Filas Para La Sección #{index}: '))
        seats = int(input(f'Asientos Para La Fila #{index}: '))
        
        # Condicional Para Válidar Los Datos Ingresados
        if (rows < 1 or seats < 1):
            raise Exception('Los Datos Ingresados Son Erróneos.')

        # Estructura Algorítmica Cíclica (for Anidado Para Mostrar Información Por Consola)
        print(f'\nSección #{index}: ')
        for row in range(1, rows + 1):
            for seat in range(1, seats + 1):
                print(f'{chr(64 + row)}{seat}', end = ' ')
            print()
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle Del Error: {e}')
finally:
    print('El Bloque De Código Termino Su Ejecución.')