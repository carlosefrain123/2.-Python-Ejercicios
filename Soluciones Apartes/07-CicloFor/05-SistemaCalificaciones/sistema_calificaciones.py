# Mensaje Guía Inicial
print('*** Sistema De Calificaciones Con Rangos Válidos (De 0 A 5) ***')

# Definir E Inicializar Variables Y/O Constantes
average = 0
low_grade = 5
grade_accumulator = 0
grade_counter = 0

try:
    # Estructura Algorítmica Cíclica for
    for index in range(5):
        # Lectura, Entrada O Ingreso De Datos
        grade = float(input(f'Ingrese La Calificación Del Estudiante #{index + 1}: '))
        
        # Estructura Algorítmica Condicional Compuesto (Válidar Calificación)
        if (grade >= 0 and grade <= 5):
            # Estructura Algorítmica Condicional Simple (Válidar Calificación Más Baja)
            if (grade < low_grade):
                low_grade = grade
            
            # Acumuladores Y Contadores
            grade_accumulator += grade
            grade_counter += 1
        else:
            print('La Calificación Ingresada No Es Válida Y No Se Va A Incluir En El Computo Final.\n')
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Algorítmica Condicional Simple (Obtener Promedio)
    if (grade_counter > 0):
        average = grade_accumulator / grade_counter 

    # Estructura Algorítmica Condicional Simple (Obtener Calificación Más Baja)
    if (grade_counter == 0):
        low_grade = 0

    # Mostrar Información Por Consola
    print(f'\nLa Cantidad De Calificaciones Registradas Correctamente Fueron: {grade_counter}')
    print(f'Promedio Del Grupo: {average}')
    print(f'Calificación Más Baja Del Grupo: {low_grade}')
finally:
    print('El Bloque De Código Termino Su Ejecución.')