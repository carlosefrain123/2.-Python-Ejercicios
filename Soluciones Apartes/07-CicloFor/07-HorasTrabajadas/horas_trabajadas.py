# Definir E Inicializar Variables Y/O Constantes
salary_one = 0
salary_two = 0
salary_three = 0
salary_four = 0
salary_accumulator = 0

try:
    # Estructura Algorítmica Cíclica for
    for index in range(4):
        # Lectura, Entrada O Ingreso De Datos
        hours_worked = int(input(f'Ingresa Las Horas Trabajadas Por El Empleado #{index + 1}: '))
        hourly_pay = float(input(f'Ingrese El Pago Por Hora Para El Empleado #{index + 1}: '))
        
        # Procesos Y Operatividad (Cálculo Del Salario)
        salary = hours_worked * hourly_pay

        # Estructura Algorítmica Condicional Match - Case
        match index:
            case 0:
                salary_one = salary
            case 1:
                salary_two = salary
            case 2:
                salary_three = salary
            case _:
                salary_four = salary
        
        # Procesos Y Operatividad (Acumulador Salario)
        salary_accumulator += salary
except Exception as e:
    print('\nLos Valores Ingresados Nos Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Mostrar Información Por Consola
    print(f'\nEl Salario Del Empleado #1: {salary_one} Dólares.')
    print(f'El Salario Del Empleado #2: {salary_two} Dólares.')
    print(f'El Salario Del Empleado #3: {salary_three} Dólares.')
    print(f'El Salario Del Empleado #4: {salary_four} Dólares.')
    print(f'El Salario Total De Los Empleados: {salary_accumulator} Dólares.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')