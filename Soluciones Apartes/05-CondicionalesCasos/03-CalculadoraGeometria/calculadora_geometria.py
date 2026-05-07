# Lectura, Entrada O Ingreso De Datos
figure = input('Nombre De La Figura (Circulo/Cuadrado/Triangulo): ').lower()

try:
    match figure:
        case 'circulo':
            # Lectura, Entrada O Ingreso De Datos
            radius = float(input('Radio Del Circulo: '))
        case 'cuadrado':
            # Lectura, Entrada O Ingreso De Datos
            side = float(input('Longitud De Un Lado Del Cuadrado: '))
        case 'triangulo':
            # Lectura, Entrada O Ingreso De Datos
            base = float(input('Base Del Triángulo: '))
            height = float(input('Altura Del Triángulo: '))   
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    match figure:
        case 'circulo':
            # Procesos Y Operaciones
            radius_area = 3.1416 * radius ** 2
            
            # Mostrar Información Por Consola
            print(f'\nÁrea Del Circulo: {radius_area} Centímetros Cuadrados.')
        case 'cuadrado':
            # Procesos Y Operaciones
            side_area = 4 * side

            # Mostrar Información Por Consola
            print(f'\nPerímetro Del Cuadrado: {side_area} Centímetros.')
        case 'triangulo':    
            # Procesos Y Operaciones
            triangle_area = (base * height) / 2 

            # Mostrar Información Por Consola
            print(f'\nÁrea Del Triángulo: {triangle_area} Centímetros Cuadrados.')
        case _:
            print('\nFigura No Soportada.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')