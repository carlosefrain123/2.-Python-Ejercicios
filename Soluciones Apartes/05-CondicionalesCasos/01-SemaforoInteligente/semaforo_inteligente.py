# Lectura, Entrada O Ingreso De Datos
color = input('Color Del Semáforo: ').lower()

# Estructura Algorítmica Condicional Casos (Validar El Tipo De Color)
match color:
    case 'rojo':
        print('\nDetener El Vehículo.')
    case 'amarillo':
        print('\nReducir La Velocidad.')
    case 'verde':
        print('\nAvanzar Con Precaución.')
    case _:
        print('\nColor No Reconocido.')