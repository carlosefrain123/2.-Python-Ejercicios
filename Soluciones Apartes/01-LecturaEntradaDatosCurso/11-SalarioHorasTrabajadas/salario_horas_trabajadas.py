try:
    # Lectura, Entrada O Ingreso De Datos
    hours_week = int(input('Ingresar La Cantidad De Horas Trabajadas En La Semana: '))
    hour_value = float(input('Ingresar El Valor Por Cada Hora Trabajada: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')   
    print(f'Detalle De La Exception: {e}')
else:
    # Procesos Aritméticos
    hours_month = hours_week * 4
    salary_base = hours_month * hour_value
    pension = salary_base * 0.03
    health = salary_base * 0.05
    salary_net = salary_base - (pension + health)

    # Mostrar Información Por Consola
    print(f'\nHoras Semanales Trabajadas => {hours_week}')
    print(f'Valor Por Hora => {hour_value} Dólares.')
    print(f'Horas Mensualmente Trabajadas => {hours_month}')
    print(f'Salario Base Del Empleado => {salary_base} Dólares.')
    print(f'Pensión => {pension} Dólares.')
    print(f'Salud => {health} Dólares.')
    print(f'Salario Neto Del Empleado => {salary_net} Dólares.')
finally:
    print('El Bloque De Código Termino Su Ejecución.\n')