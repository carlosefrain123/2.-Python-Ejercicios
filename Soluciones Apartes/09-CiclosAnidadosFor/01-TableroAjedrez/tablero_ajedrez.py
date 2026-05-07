print('****** Dibujar Un Tablero De Ajedrez ******')

try:
    # Lectura, Entrada O Ingreso De Datos
    rows = int(input('Ingrese El Número De Filas Del Tablero: '))
    columns = int(input('Ingrese El Número De Columnas Del Tablero: '))

    # Condicional Para Válidar Los Datos Ingresados
    if ((rows < 1) or (columns < 1)):
        raise Exception('Dimensiones Inválidas Para El Tablero.')
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle Del Error: {e}')
else:
    # Estructura Algorítmica Cíclica (for Anidado)
    for i in range(0, rows, 1):  
        for j in range(0, columns, 1):  
            print('■' if ((i + j) % 2 == 0) else '□', end = ' ')
        print()
finally:
    print('El Bloque De Código Termino Su Ejecución.')