try:
    # Lectura, Entrada O Ingreso De Datos
    year = int(input('Ingrese Un Año (1995): '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Operador Ternario (Validar El Año)
    leap_year = 'Sí.' if (year > 0 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)) else 'No.'

    # Mostrar Información Por Consola
    print(f'\n¿Es Un Año Bisiesto? {leap_year}')
finally:
    print('El Bloque De Código Termino Su Ejecución.')