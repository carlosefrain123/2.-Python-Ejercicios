try:
    # Lectura, Entrada O Ingreso Datos
    age = int(input('Ingrese La Edad: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Operaciones Aritméticas
    months = age * 12
    days = months * 30
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    # Mostrar Información Por Consola
    print(f'\nEdad De La Persona: {age} Años.')
    print(f'Meses De Vida: {months} Meses.')
    print(f'Días De Vida: {days} Días.')
    print(f'Horas De Vida: {hours} Horas.')
    print(f'Minutos De Vida: {minutes} Minutos.')
    print(f'Segundos De Vida: {seconds} Segundos.')
finally:
    print('El Bloque De Código Termino Su Ejecución.\n')