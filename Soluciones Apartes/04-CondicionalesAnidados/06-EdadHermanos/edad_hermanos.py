try:
    # Lectura, Entrada O Ingreso De Datos (Inicialización)
    name_one = input('Ingrese El Nombre De La Persona #1: ')
    age_one = int(input('Ingrese La Edad De La Persona #1: '))

    name_two = input('\nIngrese El Nombre De La Persona #2: ')
    age_two = int(input('Ingrese La Edad De La Persona #2: '))
except Exception as ex:
    print('\nLos Valores No Son Válidos')
    print(f'Detalle De La Excepción: {ex}')
else:
    # Estructura Condicional Compuesto (Valores No Válidos)
    if ((age_one >= 0) and (age_two >= 0) and (age_one <= 120) and (age_two <= 120)):
        # Estructura Condicional Anidado
        if (age_one > age_two):
            print(f'\nEl Hermano Mayor Es: {name_one}')
            print(f'La Edad De {name_one} Es: {age_one} Años.')
        elif (age_two > age_one):
            print(f'\nEl Hermano Mayor Es: {name_two}')
            print(f'La Edad De {name_two} Es: {age_two} Años.')
        else:
            print('\nNo Pueden Tener La Misma Edad, No Son Hermanos Gemelos.')
    else:
        print('\nLos Valores Ingresados No Son Válidos.')
finally:
    print('El Bloque De Código Termino Su Ejecución.\n')