try:
    # Lectura, Entrada O Ingreso De Datos
    weather = input('El Estado Del Clima Hoy (Lluvioso Ó Soleado): ').lower()
    via = input('¿Qué Tipo De Vía Estás Recorriendo? (Autopista Ó Ciudad): ').lower()
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Definir E Inicializar Variables Y/O Constantes
    speed = 0
    
    # Estructuras Algorítmicas Condicionales Anidados (Validando El Clima)
    if (weather == 'lluvioso' and via == 'autopista'):
        speed = 80
    elif (weather == 'lluvioso' and via == 'ciudad'):
        speed = 40
    elif (weather == 'soleado' and via == 'autopista'):
        speed = 120
    elif (weather == 'soleado' and via == 'ciudad'):
        speed = 60
    else:
        print('\nError: Datos Ingresados No Válidos.')
    
    if (speed > 0):
        print(f'\nVelocidad Máxima Permitida: {speed} km/h.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')