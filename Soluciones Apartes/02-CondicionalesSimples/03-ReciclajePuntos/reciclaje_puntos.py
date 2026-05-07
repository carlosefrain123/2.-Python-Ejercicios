try:
    device = input('Dispositivo (Celular / Laptop / Tablet): ').lower()
    state = input('¿Funciona El Dispositivo? (Si - No): ').lower()
except Exception as e:
    print('Los Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Definir E Inicializar Variables
    points = 0
    
    # Estructuras Algorítmicas Condicionales Simples
    if (device == 'celular' and (state == 'no' or state == 'si')):
        points = 10

    if (device == 'laptop' and (state == 'no' or state == 'si')):
        points = 25
    
    if (device == 'tablet' and (state == 'no' or state == 'si')):
        points = 15
    
    # Si El Funcionamiento No Es Correcto, Quitamos Puntos (Condicional Simple)
    if (state == 'no'):
        points = points / 2
    
    # Mostrar Información Por Consola (Si La Información NOOO! Es Reconocida)
    if (points == 0):
        print('\nEl Dispositivo Y/O Estado No Es Reconocido.')

    # Mostrar Información Por Consola (Si La Información Es Reconocida)
    if (points != 0):
        print(f'\nDispositivo Ingresado: {device}.')
        print(f'¿Funciona Correctamente?: {state}.')
        print(f'Los Puntos Obtenidos Son: {points} Puntos.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')