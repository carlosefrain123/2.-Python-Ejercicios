try:
    # Lectura, Entrada O Ingreso De Datos
    number = float(input('Ingrese Un Valor Numérico: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    print('\n')

    # Estructura Condicional Simple
    if ((number % 3 == 0) or (number % 5 == 0)):
        if (number % 3 == 0):
            print('El Número Ingresado Es Múltiplo Del 3.')

        if (number % 5 == 0):
            print('El Número Ingresado Es Múltiplo Del 5.')    
finally:
    print('El Bloque De Código Termino Su Ejecución.\n')