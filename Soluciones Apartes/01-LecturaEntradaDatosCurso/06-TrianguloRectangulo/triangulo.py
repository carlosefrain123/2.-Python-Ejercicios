try:
    # Lectura, Entrada O Ingreso De Datos
    base = float(input('Ingrese La Base Para El Triángulo Rectángulo: '))
    height = float(input('Ingrese La Altura Para El Triángulo Rectángulo: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Operaciones Aritméticas
    area = (base * height) / 2

    # Mostrar Información Por Consola
    print(f'\nBase Del Triángulo Rectángulo: {base} Metros.')
    print(f'Altura Del Triángulo Rectángulo: {height} Metros.')
    print(f'Área Del Triángulo Rectángulo: {area} Metros Cuadrados.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')