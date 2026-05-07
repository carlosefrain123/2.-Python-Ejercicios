print('***** Calcular Promedio De Vueltas Por Corredor *****')

try:
    # Lectura, Entrada O Ingreso De Datos
    corredores = int(input('Ingrese El Número De Corredores: '))
    vueltas = int(input('Cantidad De Vueltas Por Corredor: '))

    # Condicional Para Válidar Los Datos Ingresados
    if ((corredores < 1) or (vueltas < 1)):
        raise Exception('Los Datos Del Corredor Y/O Las Vueltas No Son Válidas.')  

    # Estructura Algorítmica Cíclica (for Anidado)
    for corredor in range(1, corredores + 1):
        total = 0
        print(f'\nCorredor #{corredor}:')
        
        for vuelta in range(1, vueltas + 1):
            tiempo = float(input(f'Tiempo (Segundos) De La Vuelta #{vuelta}: '))
            
            # Condicional Para Válidar El Tiempo En Cada Vuelta
            if (tiempo <= 0):
                raise Exception('El Tiempo Ingresado No Es Válido.')
            
            total += tiempo
        
        print(f'Promedio: {total / vueltas:.2f} Segundos.')  
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle Del Error: {e}')
finally:
    print('El Bloque De Código Termino Su Ejecución.')