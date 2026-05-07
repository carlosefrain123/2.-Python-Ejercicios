try:
    # Lectura, Entrada O Ingreso De Datos
    number = int(input('Ingresa Un Valor Numérico Entero: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Operador Ternario (Válidar El Número)
    result = 'Par' if (number % 2 == 0) else 'Impar'

    # Mostrar Información Por Consola
    print(f'\nEl Número {number} Es {result}.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')