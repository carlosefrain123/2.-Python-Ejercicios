try:
    # Lectura, Entrada O Ingreso De Datos
    age = int(input('Ingrese Su Edad: '))
    student = input('¿Tiene Carnet Estudiantil? (Si / No): ').lower()
    different_capacities = input('¿Tienes Una Capacidad Diferente O Especial? (Si / No): ').lower()
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}.')
else:
    # Definir E Inicializar Variables Y/O Constantes
    bus_rate = 0
    is_student = (student == 'si' or student == 'no')
    is_different_capacities = (different_capacities == 'si' or different_capacities == 'no')
    is_age_valid = (age >= 0 and age <= 100)

    # Estructura Algorítmica Condicional Anidado (Validar Ingreso De Datos)
    if (is_student and is_different_capacities and is_age_valid):
        # Estructura Algorítmica Condicional Anidado (Validar Categorías Prioritarias)
        if (different_capacities == 'si'):
            bus_rate = 0.50
        elif ((age >= 0) and (age <= 12)):
            bus_rate = 0.50
        elif (((age >= 13) and (age <= 25)) and student == 'si'):
            bus_rate = 1.00
        elif ((age >= 26) and (age <= 64)):
            bus_rate = 2.00
        elif (age >= 65):
            bus_rate = 0.75
        else:
            bus_rate = -1

        # Mostrar Información Por Consola
        if (bus_rate > 0):
            print(f'\nTarifa A Pagar: {bus_rate} Dólares.')
            
            if (different_capacities == 'si'):
                print('Descuento Aplicado: Persona Con Capacidades Diferentes.')
        elif (bus_rate == -1):
            print('\n⚠️ Edad Fuera Del Rango Válido (0-100).')
        else:
            print('\n❌ Datos Inconsistentes (ej: Estudiante Fuera De Rango).')
    else:
        print('\nNo Se Puede Desarrollar El Planteamiento Con Los Valores Ingresados.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')