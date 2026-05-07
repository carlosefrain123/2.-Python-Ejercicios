try:
    # Lectura, Entrada O Ingreso De Datos
    temperature = float(input('Temperatura Actual (°C): '))
    humidity = float(input('Humedad Relativa (%): '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Algorítmica Condicional Compuesto (Verificar Temperatura Alta)
    if (temperature > 35):
        print('\n¡Alerta! Temperatura Extremadamente Alta (>35°C).')
    else:
        # Estructura Algorítmica Condicional Compuesto (Verificar Temperatura Baja)
        if (temperature < 5):
            print('\n¡Alerta! Temperatura Extremadamente Baja (<5°C).')
        else:
            print('\nTemperatura Dentro Del Rango Seguro (5°C - 35°C).')
    
    # Estructura Algorítmica Condicional Compuesto (Verificar Humedad)
    if (humidity > 80):
        print('Alerta! Humedad Muy Elevada (>80%).')
    else:
        print('Humedad Dentro Del Rango Aceptable (≤80%).')
finally:
    print('El Bloque De Código Termino Su Ejecución.')