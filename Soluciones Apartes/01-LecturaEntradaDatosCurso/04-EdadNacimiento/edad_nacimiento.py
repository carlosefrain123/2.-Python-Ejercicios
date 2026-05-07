try:
    # Lectura, Entrada O Ingreso De Datos
    year_actual = int(input('Ingrese El Año Actual: '))
    year_birth = int(input('Ingrese El Año De Nacimiento: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Procesos Aritméticos
    age = year_actual - year_birth

    # Mostrar Información Por Consola
    print(f'\nMi Edad Es De {age} Años.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')