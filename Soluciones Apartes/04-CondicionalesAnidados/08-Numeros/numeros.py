try:
    # Lectura, Entrada O Ingreso De Datos
    number_one = float(input('Ingrese El Número Uno: '))
    number_two = float(input('Ingrese El Número Dos: '))
    number_three = float(input('Ingrese El Número tres: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Condicional Anidado (MAYOR)
    if ((number_one > number_two) and (number_one > number_three)):
        print(f'\nEl Número Mayor Es: {number_one}')
    elif ((number_two > number_one) and (number_two > number_three)):
        print(f'\nEl Número Mayor Es: {number_two}')
    elif ((number_three > number_one) and (number_three > number_two)):
        print(f'\nEl Número Mayor Es: {number_three}')
    else:
        print('\nTodos Los Números Ingresados Son Iguales (MAYOR)')

    # Estructura Condicional Anidado (MENOR)
    if ((number_one < number_two) and (number_one < number_three)):
        print(f'El Número Menor Es: {number_one}')
    elif ((number_two < number_one) and (number_two < number_three)):
        print(f'El Número Menor Es: {number_two}')
    elif ((number_three < number_one) and (number_three < number_two)):
        print(f'El Número Menor Es: {number_three}')
    else:
        print('Todos Los Números Ingresados Son Iguales (MENOR)')
finally:
    print('El Bloque De Código Termino Su Ejecución.\n')