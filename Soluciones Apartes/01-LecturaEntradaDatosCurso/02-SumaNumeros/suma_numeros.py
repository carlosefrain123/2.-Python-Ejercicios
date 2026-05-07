try:
    # Lectura, Entrada O Ingreso De Datos
    value_one = float(input('Ingrese El Valor Numérico #1: '))
    value_two = float(input('Ingrese El Valor Numérico #2: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Exception: {e}')
else:
    # Procesos Aritméticos
    sum = value_one + value_two

    #  Mostrar Información Por Consola
    print(f'\nNúmero Uno => {value_one}')
    print(f'Número Dos => {value_two}')
    print(f'Resultado De La Suma => {sum}')
finally:
	print('El Bloque De Código Termino Su Ejecución.')