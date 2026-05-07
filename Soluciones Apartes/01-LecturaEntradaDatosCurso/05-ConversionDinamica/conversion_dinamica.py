try:
    # Lectura, Entrada O Ingreso De Datos
    degrees_centigrade = float(input('Ingrese Los Grados Centigrados: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Procesos Aritméticos (Fórmula)
    degrees_fahrenheit  = (degrees_centigrade * 1.8) + 32

    # Mostrar Información Por Consola
    print(f'\nGrados Centigrados Iniciales => {degrees_centigrade}')
    print(f'Conversión De Centigrados A Fahrenheit => {degrees_fahrenheit}')
finally:
    print('El Bloque De Código Termino Su Ejecución.')