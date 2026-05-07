print('*** Estación Meteorológica Portátil ***')  

try:
    # Lectura, Entrada O Ingreso De Datos  
    samples = int(input('Número De Mediciones: '))

    # Condicional Para Válidar El Número De Mediciones
    if (samples <= 0):  
        raise Exception("La Cantidad Ingresada No Es Válida.")  

    # Definir E Inicializar Variables Y O Constantes
    current_sample = 0
    temp_sum = 0
    max_humidity = 0

    # Estructura Cíclica while
    while (current_sample < samples):
        # Lectura, Entrada O Ingreso De Datos
        temperature = float(input('Ingrese La Temperatura (°C): '))  
        humidity = float(input('Ingrese La Humedad Relativa (%): '))  
        pressure = float(input('Ingrese La Presión Atmosférica (hPa): '))  

        # Condicional Para Válidar Los Datos Ingresados
        if not (-50 <= temperature <= 60) or not (0 <= humidity <= 100) or pressure <= 800:  
            print('Los Valores Ingresados Están Fuera De Rango.\n')
            continue

        temp_sum += temperature

        # Condicional Para Obtener La Humedad Máxima
        if (humidity > max_humidity):
            max_humidity = humidity

        current_sample += 1
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    print('\nReporte Climático => ')
    print(f'Temperatura promedio: {temp_sum / samples}°C')
    print(f'Humedad máxima registrada: {max_humidity}%')
finally:
    print('El Bloque De Código Termino Su Ejecución.')