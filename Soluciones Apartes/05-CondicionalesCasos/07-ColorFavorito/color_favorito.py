# Construir El Menú De Opciones
print('Selecciona Del Menú De Opciones Tu Color Favorito: ')
print('1.Rojo.')
print('2.Amarillo.')
print('3.Azul.')
print('4.Verde.')
print('5.Otro')

try:
    # Definir E Inicializar Variables O Constantes
    favorite_color = int(input('Elige Una Opción Del Menú: '))
except Exception as e:
    print('\nLa Opción Ingresada No Es Válida.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Condicional CASOS
    match (favorite_color):
        case 1:
            message = 'Color Favorito ROJO.'
        case 2:
            message = 'Color Favorito AMARILLO.'
        case 3:
            message = 'Color Favorito Azul.'
        case 4:
            message = 'Color Favorito VERDE.'
        case 5:
            message = 'Color Favorito OTRO.'
        case _:
            message = 'La Opción Ingresada No Es Válida.'

    # Mostrar Información Por Consola
    print(message)
finally:
    print('El Bloque De Código Termino Su Ejecución.')