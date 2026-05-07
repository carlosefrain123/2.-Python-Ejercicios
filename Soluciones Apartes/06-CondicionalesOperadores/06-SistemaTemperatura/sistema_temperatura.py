try:
    # Lectura, Entrada O Ingreso De Datos
    temp = float(input('Ingresa La Temperatura Actual (°C): '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Operador Ternario (Validar El Estado De La Temperatura)
    temperature_status = ('Congelado' if (temp <= 0) else 'Frío' if (temp < 15) else 'Templado' if (temp < 25) else 'Caliente')

    # Mostrar Información Por Consola
    print(f'\nEstado Del Clima: {temperature_status}.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')