try:
    # Definir E Inicializar Variables
    day = int(input('Ingrese Un Número Del 1 Al 7, Para Obtener El Día De La Semana: '))
except Exception as e:
    print('\nEl Valor Ingresado No Es Válido.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Condicional Casos
    match (day):
        case 1:
            message = 'Hoy Es LUNES.'
        case 2:
            message = 'Hoy Es MARTES.'
        case 3:
            message = 'Hoy Es MIÉRCOLES.'
        case 4:
            message = 'Hoy Es JUEVES.'
        case 5:
            message = 'Hoy Es VIERNES.'
        case 6:
            message = 'Hoy Es SABADO.'
        case 7:
            message = 'Hoy Es DOMINGO.'
        case _:
            message = 'El Valor Ingresado No Es Válido.'

    # Mostrar Información Por Consola
    print(message)
finally:
    print('El Bloque De Código Termino Su Ejecución.')