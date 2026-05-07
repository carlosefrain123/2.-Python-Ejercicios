try:
    # Lectura, Entrada O Ingreso De Datos (Inicialización)
    number = float(input('Ingrese Un Valor Numérico: '))
except Exception as e:
    print('\nEl Valor Ingresado No Es Válido.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Condicional Compuesto
    if (number % 2 == 0):
        print(f'\nEl Valor Ingresado Es: {number}')
        print('El Número Ingresado Es Par.')
    else:
        print(f'\nEl Valor Ingresado Es: {number}')
        print('El Número Ingresado Es Impar.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')