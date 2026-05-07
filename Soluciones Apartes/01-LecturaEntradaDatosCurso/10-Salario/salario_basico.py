name = input('Ingrese El Nombre: ')

try:
    # Lectura, Entrada O Ingreso De Datos    
    basic_salary = float(input('Ingrese El Salario Básico: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Operaciones Aritméticas
    deduction = basic_salary * 0.12
    bonus = basic_salary * 0.023
    net_salary = (basic_salary + bonus) - deduction

    # Mostrar Información Por Consola
    print(f'\nEl Salario Básico Del Empleado Es: {basic_salary} Dólares.')
    print(f'Retención Del 12%: {deduction} Dólares.')
    print(f'Bonificación Del 2.3%: {bonus} Dólares.')
    print(f'Salario Neto Del Empleado: {net_salary} Dólares.')
finally:
    print('El Bloque De Código Termino Su Ejecución.\n')