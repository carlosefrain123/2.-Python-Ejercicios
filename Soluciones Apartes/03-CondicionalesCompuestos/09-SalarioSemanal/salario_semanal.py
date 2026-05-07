try:
    # Lectura, Entrada O Ingreso De Datos (Inicialización)
    hours = int(input('Ingrese Las Horas De La Semana: '))
except Exception as e:
    print('\nEl Valor Ingresado No Es Válido.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Condicional Compuesto (NEGATIVOS)
    if (hours >= 0):
        # Estructura Condicional Compuesto
        if (hours <= 40):
            salary = hours * 300

            # Mostrar Información
            print(f'\nCantidad De Horas Semanales: {hours}')
            print(f'Salario Semanal: {salary} Dólares.')
        else:
            salary = 40 * 300
            
            extra_hours = hours - 40
            extra_salary = extra_hours * 500

            total_salary = salary + extra_salary

            # Mostrar Información Por Consola
            print(f'\nCantidad De Horas Semanales: {hours}')
            print(f'Salario Básico Semanal: {salary} Dólares.')
            print(f'Cantidad Horas Extras: {extra_hours}')
            print(f'Salario Extra: {extra_salary} Dólares.')
            print(f'Salario Semanal Total: {total_salary} Dólares.')
    else:
        print('\nNo Es Posible Trabajar Con Valores Negativos.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')