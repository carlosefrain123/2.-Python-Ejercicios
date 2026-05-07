try:
    # Lectura, Entrada O Ingreso De Datos (Inicialización)
    age = int(input('Ingrese La Edad: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Condcional Anidado
    if ((age >= 0) and (age < 10)):
        print('\nEres Un Niño O Niña.')
    elif ((age >= 10) and (age <= 14)):
        print('\nEres Un Preadolescente.')
    elif ((age >= 15) and (age <= 18)):
        print('\nEres Un Adolescente.')
    elif ((age >= 19) and (age <= 50)):
        print('\nEres Un Adulto.')
    elif ((age > 50) and (age <= 120)):
        print('\nEres Un Adulto Mayor.')
    else:
        print('\nLa Edad Ingresada No Es Válida.')
finally:
    print('El Bloque De Código Termino Su Ejecución.\n')