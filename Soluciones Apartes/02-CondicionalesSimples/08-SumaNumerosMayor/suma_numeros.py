try:
    # Lectura, Entrada O Ingreso De Datos
    value_one = float(input('Ingrese El Primer Valor: '))
    value_two = float(input('Ingrese El Segundo Valor: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Condicional Simple
    if (value_one > value_two):
        sum = value_one + value_two
        print(f'\nLa Suma De Los Valores Ingresados Es => {sum}')

    # Estructura Condicional Simple
    if (value_two > value_one):
        multiplication = value_two * value_one
        print(f'\nLa Multiplicación De Los Valores Ingresados Es => {multiplication}')
finally:
    print('El Bloque De Código Termino Su Ejecución.\n')