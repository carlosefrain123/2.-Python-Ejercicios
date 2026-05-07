try:
    # Lectura, Entrada O Ingreso De Datos
    number = float(input('Ingrese Un Valor Numérico: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Operador Ternario (Válidar El Valor Numérico)
    sign = ('Positivo' if (number > 0) else 'Negativo' if (number < 0) else 'Cero')

    # Mostrar Información Por Consola
    print(f'\nEl Número Ingresado Es: {sign}.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')