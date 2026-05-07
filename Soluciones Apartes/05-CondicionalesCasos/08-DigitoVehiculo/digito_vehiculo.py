try:
    # Definir E Inicializar Variables
    license_plate = int(input('Ingrese El Último Digito De Una Placa: '))
except Exception as e:
    print('\nEl Valor Ingresado No Es Válido.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Condicional CASOS
    match (license_plate):
        case (license_plate) if ((license_plate == 0) or (license_plate == 1)):
            message = 'Tienes Pico Y Placa El LUNES.'
        case (license_plate) if ((license_plate == 2) or (license_plate == 7)):
            message = 'Tienes Pico Y Placa El MARTES.'
        case (license_plate) if ((license_plate == 9) or (license_plate == 4)):
            message = 'Tienes Pico Y Placa El MIÉRCOLES.'
        case (license_plate) if ((license_plate == 5) or (license_plate == 3)):
            message = 'Tienes Pico Y Placa El JUEVES.'
        case (license_plate) if ((license_plate == 6) or (license_plate == 8)):
            message = 'Tienes Pico Y Placa El VIERNES.'
        case _:
            message = 'El Valor Ingresado No Es Válido.'

    # Mostrar Información Por Consola
    print(message)
finally:
    print('El Bloque De Código Termino Su Ejecución.')