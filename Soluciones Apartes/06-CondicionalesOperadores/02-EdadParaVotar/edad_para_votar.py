try:
    # Lectura, Entrada O Ingreso De Datos
    age = int(input('Ingrese La Edad: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    if (age >= 0 and age <= 120):
        # Operador Ternario (Válidar La Edad)
        message = '\nPuedes Votar.' if (age >= 16) else '\nNo Puedes Votar.'

        # Mostrar Información Por Consola
        print(message)
    else:
        print('\nLa Edad Ingresada No Es Válida.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')