try:
    # Lectura, Entrada O Ingreso De Datos
    years = int(input('Años De Permanencia Del Empleado: '))
    sales = float(input('Ventas Mensuales Del Empleado: '))
    employee_month = input('¿Es Empleado Del Mes? (Si / No): ').lower()
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Definir E Inicializar Variables Y/O Constantes
    bonus = 0

    # Estructura Algorítmica Condicional Compuesto (Validando Una Edad Correcta)
    if ((years >= 0 and sales >= 0) and (employee_month == 'si' or employee_month == 'no')):
        # Estructura Algorítmica Condicional Compuesto (Validando Años - Ventas - Empleado Mes)
        if ((years > 5 and sales > 10000) or employee_month == 'si'):
            bonus = 500
        else:
            bonus = 0

        # Mostrar Información Por Consola
        print(f'\nAños De Permanencia: {years}.')
        print(f'Ventas Mensuales: {sales} Dólares.')
        print(f'¿Es Empleado Del Mes?: {employee_month}.')
        print(f'Bono Asignado: {bonus} Dólares.')
    else:
        print('\nInconsistencias Con El Ingreso De Los Valores O Datos.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')