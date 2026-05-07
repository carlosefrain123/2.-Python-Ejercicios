print('**** Calcular El Stock Total Por Pasillo Y Categoría ****')

try:
    # Lectura, Entrada O Ingreso De Datos
    pasillos = int(input('Ingrese El Número De Pasillos: '))
    categorias = int(input('Ingrese La Cantidad De Categorías Por Pasillo: '))
    
    # Condicional Para Válidar Los Datos Ingresados
    if ((pasillos < 1) or (categorias < 1)):
        raise Exception('Los Datos De Pasillos Y/O Categorias No Son Válidos.') 

    # Estructura Algorítmica Cíclica (for Anidado)
    for pasillo in range(1, pasillos + 1):
        total_pasillo = 0

        print(f'\nPasillo #{pasillo}: ')
        for categoria in range(1, categorias + 1):  
            stock = int(input(f'Productos En Stock De La Categoría #{categoria}: '))
            
            # Condicional Para Válidar
            if (stock < 0):  
                raise Exception('El Dato En Stock No Es Válido.')
            
            total_pasillo += stock
        
        print(f'Total Productos En Stock Del Pasillo #{pasillo}: {total_pasillo}')
except Exception as error:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle Del Error: {error}')
finally:
    print('El Bloque De Código Termino Su Ejecución.')