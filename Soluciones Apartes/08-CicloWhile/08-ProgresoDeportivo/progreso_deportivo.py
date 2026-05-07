print('*** Sistema De Seguimiento Deportivo ***')  

try:
    # Lectura, Entrada O Ingreso De Datos  
    training_weeks = int(input('Semanas De Entrenamiento: '))  
    
    # Condicional Para Válidar Las Semanas Ingresadas
    if (training_weeks <= 0):
        raise ValueError("Semanas Ingresadas No Son Válidas.")

    # Definir E Inicializar Variables Y/O Constantes
    current_week = 1  
    total_distance = 0
    max_speed = 0

    # Estructura Cíclica while 
    while (current_week <= training_weeks):
        print(f'\nSemana #{current_week}:')
        
        # Lectura, Entrada O Ingreso De Datos  
        daily_distance = float(input('Km recorridos (Promedio Diario): '))  
        peak_speed = float(input('Velocidad Máxima (km/h): ')) 

        # Condicional Para Válidar Datos Ingresados
        if (daily_distance <= 0 or peak_speed <= 0):  
            print('Los Valores Ingresados Deben Ser Positivos.')  
            continue

        total_distance += daily_distance * 7
        
        # Condicional Para Asignar La Velocidad Máxima Alcanzada
        if (peak_speed > max_speed):  
            max_speed = peak_speed  

        current_week += 1
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Mostrar Información Por Consola
    print(f'\nResumen Final:')
    print(f'Distancia Total: {total_distance} km')
    print(f'Velocidad Máxima Alcanzada: {max_speed} km/h')
finally:
    print('El Bloque De Código Termino Su Ejecución.')